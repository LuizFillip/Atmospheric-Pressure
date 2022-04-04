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
    Read data and get latitudes and longitudes
    for each sites using the get_coords funcitons from 
    'GeoMagCoords' modulus
    """
    
    def find_between(s, first, last):
        "Find string between two substrings [duplicate]"
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
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


def get_infos_by_files(filenames):
    
    '''
    filenames = ['ceeu0151.txt', 'eesc0151.txt',  
            'msbl0151.txt', 'topl0151_n.txt',
            'msnv0151.txt', 'mtca0151.txt', 
            'prma0151.txt', 'prur0151.txt',  
            'rsal0151.txt', 'seaj0151.txt',  
            'smar0151.txt', 'spfr0151.txt',]
    
    '''
    
    
    df = pd.read_csv('PressureAnalysis/Database/status/stations.txt', 
                      delim_whitespace = True)
    
    df = df.drop_duplicates(subset=['acronym'])
    
    df = df.dropna()
    
    result = []
    for num in range(len(df)):
        name = df.iloc[num]['site']
        acc = df.iloc[num]['acronym']
        lat =  df.iloc[num]['Lat']
        lon =  df.iloc[num]['Lon']
        
        if any(s[:4].upper() == acc for s in filenames):
    
            result.append([name, acc, float(lat), float(lon)])
    

    return np.array(result)


    
       