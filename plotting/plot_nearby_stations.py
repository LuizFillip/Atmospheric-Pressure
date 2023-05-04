# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:13:28 2022

@author: Luiz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PressureAnalysis.remove_lines import *

files = ['sms15jan.22m', 'smar0151.txt', 
        'vss15jan.22m',  'eesc0151.txt', 
        'ara15jan.22m', 'topl0151_n.txt', 
        'eus15jan.22m', 'ceeu0151.txt']

pre_infile = 'PressureAnalysis/Database/station_data_brasil/'
mag_infile = 'MagnetometerAnalysis/Database/Magnetometer15012022/'

import PressureAnalysis.pressureAnalysis as pr


sys.path.insert(1, 'MagnetometerAnalysis')

import Embrace as mg

nrows = 4
ncols = 2

fig, axs = plt.subplots(figsize = (12, 10), 
                      nrows = nrows, 
                      ncols = ncols)

plt.subplots_adjust(hspace = 0, wspace = 0)

remove_lines(axs, nrows, ncols)

x = np.array([['Rio Grande', 'rga', -53.78, -67.70],
                ['São Martinho da Serra/RS', 'sms', -29.53,-53.85], 
                ['Tucumán', 'tcm', -26.56, -64.88], 
                ['São José Dos Campos', 'sjc', -23.19, -45.89], 
                ['Vassouras/RJ', 'vss', -22.41, -43.66],
                ['Jataí', 'jat', -17.88, -51.72], 
                ['Cuiabá', 'cba', -15.60, -56.10], 
                ['Araguatins/TO', 'ara', -5.65, -48.12], 
                ['Eusébio/CE', 'eus',  -3.89, -38.45], 
                ['São Luis', 'slz', -2.53, -44.30],
                ["Pilar", "pil", -31.7, -63.89],
                ["Tatuoca", "ttb", -1.205, -48.51]])

axs[0, 0].set(title = 'EMBRACE Magnetometers')
axs[0, 1].set(title = 'IBGE Stations')
for num, ax in enumerate(axs.flat):
    
    filename = files[num]
    
    if '15jan.22m' in filename:
        infile = mag_infile
        df = mg.setting_dataframe(infile, filename)
    
        ax.plot(df['dtrend'], color = 'k', lw = 1)
        name = x[(x[:, 1] == filename[:3])][0][0]
                
        ax.set(ylim = [-10, 10])
    else:
        infile = pre_infile
        ax1 = ax.twinx()
        df = pr.setting_dataframe(infile, filename)
    
        ax1.plot(df['dtrend'], color = 'k', lw = 1)
        name = infos_met(filename).infos[0]
        
        if num == 1:    
            ax1.spines['bottom'].set_visible(False)  
            ax1.spines['left'].set_visible(False)
        elif num == (nrows*ncols - 1):    
            ax1.spines['top'].set_visible(False)
            ax1.spines['left'].set_visible(False)
        elif num // 2 != 0:
            ax1.spines['top'].set_visible(False)
            ax1.spines['bottom'].set_visible(False)
            ax1.spines['left'].set_visible(False)
            
        
        ax1.set(ylim = [-1, 0.9])
    
    ax.text(0.03, 0.8, name, transform = ax.transAxes)

    ax.xaxis.set_major_formatter(dates.DateFormatter('%H'))
    ax.xaxis.set_major_locator(dates.HourLocator(interval = 2))
    
    
fig.text(0.06, 0.5, 'Horizontal component (nT)', va='center', 
             rotation='vertical', fontsize = fontsize)   

fig.text(0.97, 0.5, 'Pressure variation (mbar)', va='center', 
             rotation='vertical', fontsize = fontsize)   

fig.text(0.45, 0.08, 'Universal time (UT)', va='center', 
             rotation='horizontal', fontsize = fontsize) 

fig.suptitle(f'dTrend Analysis - 15/01/2022', 
             y = 0.94, fontsize = 20)


path_to_save = 'PressureAnalysis/Figures/'
 
plt.savefig(path_to_save + 'MagnetometersPressureDtrend.png', 
         dpi = 100, bbox_inches="tight")