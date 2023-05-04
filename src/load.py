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

import matplotlib.pyplot as plt

infile = "database/Pressure/"

def plot_timeseries(ax, infile, col, name = "Cariri",
                    sites = ["rnna", "seaj"]):
    
    for index, site in enumerate(sites):
        
        filename = f"{site}0151.22m"
        df = load_data(os.path.join(infile, filename))
        
        dtrend(df)["dtrend"].plot(ax = ax[index, col])
        
        ax[index, col].text(0.05, 0.85, site.upper(), 
                            transform = ax[index, col].transAxes
                            )
        ax[index, col].axhline(0, linestyle = "--")
        
    ax[1, col].set_xlabel("Time (UT)", fontsize = 20)
    ax[0, col].set(title = name, ylim = [-1, 1])
    
    
fig, ax = plt.subplots(
    ncols = 2, 
    nrows = 2, 
    dpi = 300, 
    figsize = (12, 5), 
    sharey = True, 
    sharex = True
    
    )

plt.subplots_adjust(
    hspace = 0.05,
    wspace = 0.05)

plot_timeseries(ax, infile, col = 0, sites = ["rnna", "seaj"])

plot_timeseries(ax, infile, col = 1, name = "Cachoeira Paulista",
                sites = ["spfr", "eesc"])    

fontsize = 20
fig.text(0.05, 0.5, 'Pressure Displecement (mbar)', va='center', 
             rotation = 'vertical', fontsize = fontsize)   

fig.savefig("dtrend.png", dpi = 400)