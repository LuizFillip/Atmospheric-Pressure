# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 11:35:53 2022

@author: LuizF
"""
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import sys
import os
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


from PressureAnalysis.pressureAnalysis import *


files =['ceeu0151.txt', 'seaj0151.txt', 
        'topl0151_n.txt', 'mtca0151.txt',
        'eesc0151.txt',  'msbl0151.txt',
        'itai0151.txt', 'smar0151.txt']

files = files[::-1]

infile = 'PressureAnalysis/Database/station_data_brasil/'


def SequentialPlot(files, infile, figsize = (6, 10), save = False,
                   component = 'H', N = 10, fontsize = 13):
    
    nrows = len(files)
    files = files[::-1]
    
    fig, axs = plt.subplots(figsize = figsize, 
                           sharex = True, 
                           nrows = nrows)
    
    plt.subplots_adjust(hspace = 0)
    
    
    for ax, num in zip(axs.flat, range(nrows)):
        
        df = setting_dataframe(infile, files[num])
        
        
        ax.plot(df['dtrend'], color = 'k', lw = 1)
        

        ax.set(xlabel = 'Universal time (UT)', 
               ylim = [-1, 1])
        
        name = infos_met(files[num]).infos[0]
        #Put the name of location
        ax.text(0.03, 0.8, name, transform = ax.transAxes)
        
    
        if num == 0:    
            ax.spines['bottom'].set_visible(False)       
        elif num == (nrows - 1):    
            ax.spines['top'].set_visible(False)
        else:
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            
        ax.xaxis.set_major_formatter(dates.DateFormatter('%H'))
        ax.xaxis.set_major_locator(dates.HourLocator(interval = 2))
        
    fig.text(0.01, 0.5, 'Pressure Displecement', va='center', 
                 rotation = 'vertical', fontsize = fontsize)   
    
    fig.suptitle(f'IBGE Stations Network dTrend - 15/01/2022', 
             y = 0.91, fontsize = fontsize)
    
    if save:
        NameToSave = 'dTrendAnalysis.png'
        path_to_save = 'PressureAnalysis/Figures/'
        
        plt.savefig(path_to_save + NameToSave, 
                dpi = 100, bbox_inches="tight")
        

SequentialPlot(files, infile, figsize = (6, 10), save = True,
                   component = 'H', N = 10, fontsize = 13)