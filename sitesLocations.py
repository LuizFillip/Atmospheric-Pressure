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

def circle_range(ax, longitude, latitude, radius = 500):
             
    import shapely.geometry as sgeom
    from cartopy.geodesic import Geodesic

    gd = Geodesic()
    geoms = []
   
    cp = gd.circle(lon = longitude, 
                   lat = latitude, 
                   radius = radius * 1000.)

    geoms.append(sgeom.Polygon(cp))

    ax.add_geometries(geoms, crs=ccrs.PlateCarree(), 
                      edgecolor = 'black', 
                      alpha=0.3, label = 'radius')




def PlotPressure(ax):
    
        
    if save: 
        NameToSave = 'LocationsMagnetometersAndPressure.png'
        path_to_save = 'PressureAnalysis/Figures/'
        
        plt.savefig(path_to_save + NameToSave, 
                dpi = 100, bbox_inches="tight")
        

start_lat, end_lat = -60, 20
start_lon, end_lon = -75, -30 
step_lat, step_lon = 5, 5
    

# Get map properities routine from SitesLocations
fig, ax = features_of_map(start_lon, end_lon, step_lon, 
                          start_lat, end_lat, step_lat)    

fontsize = 14
# Plot meteorology stations (pressure) points 

# Plot EMbrace magnetometers points 
#Plot_EMBRACE(fig, ax, fontsize = fontsize)

# Brazilian stations of intermagnet 
files_intermagnet = ['pil20220115pmin.min.txt', 'ttb20220115qmin.min']
    
#Plot_from_files(fig, ax, files_intermagnet, 'MagnetometerAnalysis/Database/Intermag/', 
#                dip = True, fontsize = fontsize, save = False)


#ax.legend(loc = 'center')