# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:06:45 2022

@author: LuizF
"""

import cartopy.feature as cf
import cartopy.crs as ccrs
import datetime
import time

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from MagnetometerAnalysis.SitesLocations import *

def PlotMap(lat, lon, name):
    
    size = 13
    
    ax.plot(lon, lat, 'o', color = 'red', 
                    marker = '^', markersize = size)
        
    offset = 1
    ax.text(lon + 1, lat, name, fontsize = size)
        

df = pd.read_csv("Database/Stations.dat", delim_whitespace= True)

stations = ['braz0151.txt', 'ceeu0151.txt', 'eesc0151.txt', 'itai0151.txt', 
         'msaq0151.txt', 'msbl0151.txt', 'msjr0151.txt', 'msmn0151.txt', 
         'msnv0151.txt', 'mspm0151.txt', 'mspp0151.txt', 'mtca0151.txt', 
         'mtsc0151.txt', 'prma0151.txt', 'prur0151.txt', 'rnna0151.txt', 
         'rsal0151.txt', 'seaj0151.txt', 'sjrp0151.txt', 'smar0151.txt', 
         'spfr0151.txt', 'topl0151_n.txt']


sts = pd.read_csv('Database/status/stations.txt', 
                  delim_whitespace = True)

sts = sts.dropna()

start_lat, end_lat = -30, 0 
start_lon, end_lon = -60, -30 
step_lat, step_lon = 5, 5
    
fig, ax = features_of_map(start_lon, end_lon, step_lon, 
                          start_lat, end_lat, step_lat)    

for num in range(len(sts)):
    name = sts.iloc[num]['site']
    acc = sts.iloc[num]['acronym']
    lat =  sts.iloc[num]['Lat']
    lon =  sts.iloc[num]['Lon']
    if any(s[:4].upper() == acc for s in stations):
        PlotMap(float(lat), float(lon), name)

