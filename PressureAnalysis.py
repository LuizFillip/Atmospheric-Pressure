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



infile = 'Database/station_data_brasil/'

stations = ['SMAR','MSMN','MTCA','SPFR']

def select_files(stations, infile):
    
    _, _, files = next(os.walk(infile))
    
    out = []
    for filename in files:
        if any(sts.lower() in filename for sts in stations):
            out.append(filename)
            
    return out

files = select_files(['0151'], infile)

for filename in files:
    acronym = filename[:4].upper()
    


