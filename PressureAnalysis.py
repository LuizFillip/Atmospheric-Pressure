# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:30:20 2022

@author: LuizF
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


infile = 'station_data_brasil/'


   

stations = ['SMAR','MSMN','MTCA','SPFR']

def read_files(stations, infile):
    _, _, files = next(os.walk(infile))
    
    for filename in files:
        if any(sts.lower() in filename for sts in stations):
            print(filename)
            
    return 

_, _, files = next(os.walk(infile))

filename = files[0]
df = pd.read_csv(infile + filename, 
                 delim_whitespace = True, 
                 columns = ['time', ]) 
#print(df)

