# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:12:33 2022

@author: LuizF
"""

import os
import pandas as pd


import sys

infile = ('C:/Users/LuizF/Google Drive/My Drive/' + 
  'Python/code-master/JunkCode/')

sys.path.insert(1, infile)

from GeoMagCoords import *
    


def get_status(infile, filename):
    
    """
    Read data and find latitudes and longitudes
    for each sites
    """
    
    def find_between(s, first, last):
        "Find string between two substrings [duplicate]"
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""
    
    with open(infile + filename,  encoding='utf-8') as f:
        data = [line.strip()
                for line in f.readlines()]
    
    result = []
    for s in data:
        if s != '':
            site = find_between(s, "(", ")" )
            acronym = s[:4].strip()
            status = find_between(filename, "names_", ".txt" )
            
            try:
                lat_geo, lon_geo = get_coords(site, 'Brazil')
            except:
                lat_geo, lon_geo = np.nan, np.nan

            result.append([site, acronym, lat_geo, lon_geo, status])
            
    return pd.DataFrame(result, columns = ['site', 'acronym', 
                                           'Lat', 'Lon', 'status'])

def main(infile):

    output = []
    _, _, files = next(os.walk(infile))
    
    for filename in files:
        output.append(get_status(infile, filename)) 

    return pd.concat(output)

infile = 'Database/status/'


df = main(infile)

print(df.to_csv(infile + 'stations.txt', sep = ' '))