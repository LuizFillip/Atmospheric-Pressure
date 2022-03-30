# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:30:20 2022

@author: LuizF
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


infile = 'Database/station_data_brasil/'


   

stations = ['SMAR','MSMN','MTCA','SPFR']

def select_files(stations, infile):
    
    _, _, files = next(os.walk(infile))
    
    out = []
    for filename in files:
        if any(sts.lower() in filename for sts in stations):
            out.append(filename)
            
    return out

#
#df = pd.read_csv(infile + filename, 
#                 delim_whitespace = True) 

files = select_files(['151'], infile)
    
filename = files[0]

df = pd.read_csv(infile + filename, delimiter=" ", header=None)

df.index = pd.to_datetime(df[0])


df = df[[0,1]]

print(df.head())

df[1].plot()