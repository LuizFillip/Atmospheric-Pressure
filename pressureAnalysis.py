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



def setting_dataframe(infile, filename, 
                      component = 'PR', N = 10):



    df = pd.read_csv(infile + filename, 
                     header = 0,
                     delim_whitespace = True, 
                     names = ['PR', 'TD', 'HR']) 
    
    df.index = pd.to_datetime(df.index)
    
    
    df['dtrend'] = (df[component] - df[component].rolling(window = N).mean())
    
    df['time'] = df.index.hour + (df.index.minute / 60)
    
    df = df.dropna()
    
    
    return df




class infos_met:
    def __init__(self, filename = None):
        # ['Franca/SP', 'SPFR', -20.53, -47.47], 
        # ['Umuarama/PR', 'PRUR', -23.76, -53.31], 
        self.infos_ = np.array([['Eusébio/CE', 'CEEU', -3.89, -38.45], 
                          ['Palmas/TO', 'TOPL', -10.18, -48.33], 
                          ['Aracaju/SE', 'SEAJ', -10.92, -37.08], 
                          ['Carceres/MG', 'MTCA', -20.13, -50.51],
                          ['Bela Vista/MS', 'MSBL', -22.11, -56.53],
                          ['São Carlos/SP', 'EESC', -22.02, -47.89],
                          ['Santa Maria/RS', 'SMAR', -29.71, -53.71], 
                          ['Foz do Iguaçu/PR', 'ITAI', -25.42, -54.58]])
        
        if filename is not None:
            self.acc = filename
            
            self.cond = self.infos_[(self.infos_[:, 1] == 
                                     self.acc[:4].upper())][0]
        
    @property
    def infos(self):
        return self.cond
    
    @property
    def sites_names(self):
        return self.infos_[:, 0]
    @property
    def acronyms(self):
        return self.infos_[:, 1]
    @property
    def latitudes(self):
        return pd.to_numeric(self.infos_[:, 2])
    @property
    def longitudes(self):
        return pd.to_numeric(self.infos_[:, 3]) 
    


