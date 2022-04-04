# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 22:52:21 2022

@author: LuizF
"""

import matplotlib.pyplot as plt

def remove_lines(ax, nrows, ncols):
    
    '''
    Remove inferior and superior lines (spines) from the subplots
    with the exception the firt (must have the top spine)
    and the last one, must have the bottom, only. 
    '''

    if ncols > 1: 
        for x in range(nrows):
            for y in range(ncols):
                if y == 0:
                    ax[x, y].spines['right'].set_visible(False)
                    if x == 0: 
                        ax[x, y].spines['bottom'].set_visible(False)
                    elif x == (nrows - 1):
                        ax[x, y].spines['top'].set_visible(False)   
                    else:
                        ax[x, y].spines['top'].set_visible(False)   
                        ax[x, y].spines['bottom'].set_visible(False)  
                        
                else:
                    ax[x, y].spines['left'].set_visible(False)
                    if x == 0: 
                        ax[x, y].spines['bottom'].set_visible(False)
                        ax[x, y].axes.yaxis.set_visible(False)
                    elif x == (nrows - 1):
                        ax[x, y].spines['top'].set_visible(False)   
                        ax[x, y].axes.yaxis.set_visible(False)
                    else:
                        ax[x, y].spines['top'].set_visible(False)   
                        ax[x, y].spines['bottom'].set_visible(False)  
                        ax[x, y].axes.yaxis.set_visible(False)
                        
    else:
        for num in range(nrows):
            if num == 0:    
                ax[num].spines['bottom'].set_visible(False)       
            elif num == (nrows - 1):    
                ax[num].spines['top'].set_visible(False)
            else:
                ax[num].spines['top'].set_visible(False)
                ax[num].spines['bottom'].set_visible(False)
                
def main():
    nrows = 4
    ncols = 1
    fig, ax = plt.subplots(figsize = (12, 10), 
                           sharex = True, sharey = True,
                           nrows = nrows, ncols = ncols)
    
    plt.subplots_adjust(hspace = 0, wspace = 0)
     
    remove_lines(ax, nrows, ncols)

