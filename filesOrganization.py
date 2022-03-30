# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 15:12:33 2022

@author: LuizF
"""

import os
import pandas as pd




def get_status(infile, filename):
    
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
    
            result.append([site, acronym, status])
            
    return pd.DataFrame(result, columns = ['site', 'acronym', 'status'])

def main(infile):

    output = []
    _, _, files = next(os.walk(infile))
    
    for filename in files:
        output.append(get_status(infile, filename)) 

    return pd.concat(output)

infile = 'Database/status/'


df = main(infile)

print(df.to_csv(infile + 'stations.txt', sep = ' '))