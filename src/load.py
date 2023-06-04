import pandas as pd
import os 


def load_data(infile):
    f = open(infile).read()
    
    head = f.find("END OF HEADER")  
    
    data = f[head:].split("\n")[1:]
    out1 = []
    for row in data:
        out = []
        out1.append(out)
        for item in row.split():
            out.append(item)
                
    df = pd.DataFrame(out1)
                
    df = df.iloc[:-1, 0:8]
        
    df = df.apply(pd.to_numeric, errors='coerce')
    
    df.index = df[3] + (df[4] / 60)
    
    return df.loc[:, [6, 7]]



def dtrend(df, c = 6, N = 10):

    df['dtrend'] = (df[c] - df[c].rolling(window = N).mean())
    return df

