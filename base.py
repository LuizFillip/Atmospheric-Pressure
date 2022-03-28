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
import sys


sys.path.insert(1, 'MagnetometerAnalysis/')

from SitesLocations import *


start_lat, end_lat = -60, -35 #-60, 10
start_lon, end_lon = -60, -30 #-80, -30
step_lat, step_lon = 5, 5




df = pd.read_csv('PressureAnalysis/rel_station.csv', 
                 delimiter = ';', header = 1)

print(df)

def main():
    
    fig, ax = features_of_map(start_lon, end_lon, step_lon, 
                start_lat, end_lat, step_lat)    
    
    for num in range((len(df))):
        
        size = 20
        
        lon = df.lon.values[num]
        lat = df.lon.values[num]
        name = df.Estacao.values[num]
        
        ax.plot(lon, lat, 'o', color = 'red', 
                    marker = '^', markersize = size)
        
        offset = 1
        ax.text(lon + 1, lat, name, fontsize = size)
        
#main()