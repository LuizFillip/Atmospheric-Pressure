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



#df = pd.read_csv("Database/Stations.dat", delim_whitespace= True)


start_lat, end_lat = -30, 0 
start_lon, end_lon = -60, -30 
step_lat, step_lon = 5, 5
    
fig, ax = features_of_map(start_lon, end_lon, step_lon, 
                          start_lat, end_lat, step_lat)    

def PlotMap(ax):
    
    stations = ['braz0151.txt', 'ceeu0151.txt', 'eesc0151.txt', 'itai0151.txt', 
         'msaq0151.txt', 'msbl0151.txt', 'msjr0151.txt', 'msmn0151.txt', 
         'msnv0151.txt', 'mspm0151.txt', 'mspp0151.txt', 'mtca0151.txt', 
         'mtsc0151.txt', 'prma0151.txt', 'prur0151.txt', 'rnna0151.txt', 
         'rsal0151.txt', 'seaj0151.txt', 'sjrp0151.txt', 'smar0151.txt', 
         'spfr0151.txt', 'topl0151_n.txt']


    sts = pd.read_csv('PressureAnalysis/Database/status/stations.txt', 
                      delim_whitespace = True)

    sts = sts.dropna()   
    for num in range(len(sts)):
        name = sts.iloc[num]['site']
        acc = sts.iloc[num]['acronym']
        lat =  float(sts.iloc[num]['Lat'])
        lon =  float(sts.iloc[num]['Lon'])
        
        if any(s[:4].upper() == acc for s in stations):
         
            size = 12
        
            ax.plot(lon, lat, 'o', color = 'red', 
                            marker = '^', markersize = size)
                
            offset = 1
            ax.text(lon + 1, lat, name, fontsize = size)
        
PlotMap(ax)    
        
def circle(ax, 
           latitude, 
           longitude, 
           radius = 500):
    
    import shapely.geometry as sgeom
    from cartopy.geodesic import Geodesic

    gd = Geodesic()
    geoms = []
    for num in range(len(latitude)):
    
        cp = gd.circle(lon = longitude[num], 
                       lat = latitude[num], 
                       radius = radius * 1000.)
    
        geoms.append(sgeom.Polygon(cp))

        ax.add_geometries(geoms, crs=lcc, edgecolor = 'black', 
                          alpha=0.3, label = 'radius')

circle(ax, latitude, longitude, radius)