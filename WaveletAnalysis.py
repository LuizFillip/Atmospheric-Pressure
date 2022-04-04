# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:51:38 2022

@author: LuizF
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:23:32 2022

@author: LuizF
"""
import os.path
import sys
import matplotlib.ticker as ticker
import matplotlib as mpl
from pylab import *

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from PressureAnalysis.pressureAnalysis import *

from PressureAnalysis.remove_lines import *

def Wavelet(df, ax = None, 
                 transform = 'power', 
                 maximum_period = 1.1, 
                 minimum_period = 0.1):
    
    '''
    Compute and plot wavelet analysis
    software from Torrence and Compo 1998. 
    
    '''
    
    wavelet_path = 'C:\\Users\\LuizF\\Google Drive\\My Drive\\'\
    'Python\\code-master\\wavelets-master\\wave_python\\'
    
    sys.path.insert(1, wavelet_path)
    from waveletFunctions import wave_signif, wavelet
    
    dt = 0.016 # sampling time (1 minute)
    sst = df['dtrend'].values
    time = df['time'].values
    pad = 1
    variance = np.std(sst, ddof=1) ** 2
    mother = 'MORLET'
    lag1 = 0.01
    s0 = 2 * dt  
    
    n  = len(sst)
    if 0:
        variance = 1.0
        sst = sst / np.std(sst, ddof=1)
     
    #wavelet transform
    wave, period, scale, coi = wavelet(sst, dt = dt, pad = pad, s0 = s0)
    
    transform = transform.lower()
    
    # Chooice between
    if transform == 'power':
        # Compute the power spectrum
        power = (np.abs(wave))**2  
        
    elif transform == 'phase':
        # Compute the phase
        power = np.arctan2(np.imag(wave), np.real(wave)) 
    else:
        # Compute the amplitude
        power = np.real(wave)
        
    # Filter the periods
    condition = ((period >= minimum_period) & (period <= maximum_period))
        
    ind = np.where(condition)
    new_period = period[condition]
    new_power = power[ind, :][0]
    new_power = new_power / np.max(new_power)
 
    time = df.index

    
    if ax:
    
        levels = MaxNLocator(nbins=80).tick_values(new_power.min(), 
                                                   new_power.max())
        
        im = ax.contourf(time, new_period, new_power, 
                         levels = levels, cmap = 'jet')
        return im
    
    return time, new_period, new_power, new_sig95

        
def plot(files, infile, nrows = 4, ncols = 2, transform = 'power', 
         component = 'H', fontsize = 14, save = False):
    
    fig, ax = plt.subplots(figsize = (12, 10), 
                           sharex = True, sharey = True,
                           nrows = nrows, ncols = ncols)
    
    plt.subplots_adjust(hspace = 0, wspace = 0)
    
    remove_lines(ax, nrows, ncols)
    
    for num, ax in enumerate(ax.flat):
    
        
        df = setting_dataframe(infile, files[num])
        
    
        im = Wavelet(df, ax, transform = transform)
        
        name = infos_met(files[num]).infos[0]
        ax.text(0.03, 0.89, name, 
                      transform = ax.transAxes)
    
         
        deltatime = datetime.timedelta(minutes = 30)
        
        ax.set(ylim = [0, 1.3], 
                    xlim = [df.index[0] - deltatime, 
                            df.index[-1] + deltatime],
                     yticks = np.arange(0, 1.2, 0.2))
        
        ax.xaxis.set_major_formatter(dates.DateFormatter('%H'))   
        ax.xaxis.set_major_locator(dates.HourLocator(interval = 2))
            
            
    fig.text(0.07, 0.5, 'Period (hours)', va='center', 
                 rotation='vertical', fontsize = fontsize)   
    
    fig.text(0.4, 0.08, 'Universal time (UT)', va='center', 
                 rotation='horizontal', fontsize = fontsize) 

    
    fig.suptitle(f'Wavelet Analysis - Pressure Variation - 15/01/2022', 
                 y = 0.9, fontsize = fontsize)
    
    plt.rcParams.update({'font.size': fontsize})    
    
    
    
    if save:
          
        NameToSave = f'WaveletAnalysisPressure.png'
        
        path_to_save = 'PressureAnalysis/Figures/'
    
        plt.savefig(path_to_save + NameToSave, 
                    dpi = 100, bbox_inches="tight")
    
    
    plt.show()            
    
files = ['ceeu0151.txt', 'seaj0151.txt', 
        'topl0151_n.txt', 'mtca0151.txt',
        'eesc0151.txt',  'msbl0151.txt',
        'itai0151.txt', 'smar0151.txt']

files = files[::-1]

infile = 'PressureAnalysis/Database/station_data_brasil/'
    
    
plot(files, infile, nrows = 4, ncols = 2, transform = 'power', 
         component = 'H', fontsize = 14, save =True)
