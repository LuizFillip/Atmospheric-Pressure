# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:30:20 2022

@author: LuizF
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import subprocess

def rinex_files():
    '''
    Code Routine from Marcelo Banik de Padua (INPE)
    
    '''

    if 1 == len(sys.argv):
        message = 'usage: %s rinexMet\n' % sys.argv[0].split('/')[-1]
        message += 'read rinex met file and output\n'
        message += 'yyyy-mm-ddThh:mm:ss PR TD HR\n'
        message += 'where:\n'
        message += ' PR : Pressure (mbar)\n'
        message += ' TD : Dry temperature (deg Celsius)\n'
        message += ' HR : Relative humidity (percent)\n'
        print(message)
        sys.exit(1)

    rinex = sys.argv[1]
    N = int(subprocess.check_output(['grep', '-n', 'END OF HEADER$', rinex]
                                    ).decode('utf-8').split(':')[0])
    
    widths = [3, 3, 3, 3, 3, 3, 7, 7, 7]
    columns = ['y', 'm', 'd', 'H', 'M', 'S', 'PR', 'TD', 'HR']

    def dateparser(x): 
        return pd.datetime.strptime(x, '%y %m %d %H %M %S')
    
    met = pd.read_fwf(rinex, widths=widths, skiprows=N,
                      parse_dates=[[0, 1, 2, 3, 4, 5]],
                      date_parser=dateparser,
                      index_col='y_m_d_H_M_S',
                      names=columns)

    for row in met.itertuples():
        print('{} {} {} {}'.format(row[0].strftime('%Y-%m-%dT%H:%M:%S'),
                                   row[1], row[2], row[3]))



def setting_dataframe(infile, filename, component = 'PR', N = 30):



    df = pd.read_csv(infile + filename, 
                     header = 0,
                     delim_whitespace = True, 
                     names = ['PR', 'TD', 'HR']) 
    
    df.index = pd.to_datetime(df.index)
    
    
    df['dtrend'] = (df[component] - df[component].rolling(window = N).mean())
    
    df['time'] = df.index.hour + (df.index.minute / 60)
    
    df = df.dropna()
    
    return df




from MagnetometerAnalysis.WaveletAnalysis import *
import  MagnetometerAnalysis.Embrace as ebc

fig, ax = plt.subplots(nrows = 2, 
                       sharex = True) #sharey  = True)

plt.subplots_adjust(hspace = 0)

N = 30
fontsize = 12

## Magnetometer 
mag = ebc.setting_dataframe('MagnetometerAnalysis/Database/Magnetometer15012022/', 
                  'eus15jan.22m', component = 'H(nT)', N = N)

#Wavelet(mag, ax[0], transform = 'power')


ax[0].plot(mag['dtrend'], lw= 1, color = 'k')


ax[0].text(0.03, 0.87, 'Horizontal Component (H)', 
                         transform = ax[0].transAxes)


## Pressure variation
pr = setting_dataframe('PressureAnalysis/Database/station_data_brasil/', 
                'ceeu0151.txt', N = N)


ax[1].plot(pr['dtrend'], lw = 1, color = 'k')

#Wavelet(pr, ax[1], transform = 'power')

ax[1].text(0.03, 0.87, 'Pressure variatins (dP)', 
                         transform = ax[1].transAxes)

ax[1].set(xlabel = 'Univertal time')

ax[1].xaxis.set_major_formatter(dates.DateFormatter('%H'))
ax[1].xaxis.set_major_locator(dates.HourLocator(interval = 2))

def date(instance_, format_ = "%d/%m/%Y"):
        return instance_.date.strftime(format_)

fig.text(0.03, 0.5, 'Variation', va = 'center', 
                 rotation='vertical', fontsize = fontsize)   

fig.suptitle(f'dTrend analysis - Eusébio/CE - 15/01/2022', 
                 y = 0.92, fontsize = fontsize)
    
plt.rcParams.update({'font.size': fontsize})    

plt.savefig('PressureAnalysis/Figures/dtrend.png', 
            dpi = 100, bbox_inches="tight")