# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 13:06:45 2022

@author: LuizF
"""

import cartopy.feature as cf
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from MagnetometerAnalysis.SitesLocations import *

def circle_range(ax, longitude, latitude, 
                 radius = 500):
             
    import shapely.geometry as sgeom
    from cartopy.geodesic import Geodesic

    gd = Geodesic()

    cp = gd.circle(lon = longitude, 
                   lat = latitude, 
                   radius = radius * 1000.)
    geoms = [sgeom.Polygon(cp)]

    ax.add_geometries(geoms, crs=ccrs.PlateCarree(), 
                      edgecolor = 'black', 
                      alpha=0.3, label = 'radius')



start_lat, end_lat = -40, 10
start_lon, end_lon = -75, -30 
step_lat, step_lon = 5, 5
    

# Get map properities routine from SitesLocations
fig, ax = features_of_map(start_lon, end_lon, step_lon, 
                          start_lat, end_lat, step_lat)    


from PressureAnalysis.pressureAnalysis import *

fontsize = 15
x =  infos_met()

for lat, lon, name in zip(x.latitudes, 
                          x.longitudes, 
                          x.sites_names):
    
    ax.plot(lon, lat, marker = 'o', 
            color = 'blue', markersize = fontsize)
    offset = -1
    ax.text(lon, lat + offset, name, fontsize = fontsize)
    
    
from MagnetometerAnalysis.Embrace import *

names, acronym, lat, lon = sites_infos(remove = (3, 5))
 

for num in range(len(names)):
    
    longitude = lon[num]
    latitude = lat[num]
    name = names[num]
    if name == "Rio Grande":
        break
    
    ax.plot(longitude, latitude, 
            color = 'red', label = 'EMBRACE Mag.', 
            marker = '^', markersize = fontsize)
    
    circle_range(ax, longitude, latitude, radius = 500)
    offset = 1
    ax.text(lon[num], lat[num] + offset, 
            name, fontsize = fontsize)
    
    
    
size = 200
l1 = plt.scatter([],[], s = size, color = 'blue', edgecolors='none')
l2 = plt.scatter([],[], s = size, color = 'red', marker = '^', edgecolors='none')

labels = ["IBGE Stations", "Magnetometers"]

leg = plt.legend([l1, l2], labels, ncol=4, frameon=True, fontsize= fontsize,
                 handlelength=2, loc = 9, borderpad = 1.8,
                 handletextpad=1, title='Instrumentation', scatterpoints = 1)
    
fig.suptitle('Locations and 500 km range area', y = 0.91)

def save():    
    NameToSave = 'LocationsIBGEandMags.png'
    path_to_save = 'PressureAnalysis/Figures/'
    
    plt.savefig(path_to_save + NameToSave, 
        dpi = 100, bbox_inches="tight")
    
    
