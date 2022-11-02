import csv
import pandas as pd
import numpy as np
ball=pd.read_csv("C:/Users/sreeh/OneDrive/Desktop/final year project/IPL Ball-by-Ball 2008-2020.csv")
ball=ball.fillna(0)
ids=ball['id'].unique()
for id in ids:
    match=ball.loc[ball['id']==id]
    innings1=match.loc[match['inning']==1]
    batsmanlist=match['batsman'].unique();
    count=0
    batsmanpos={}
    batsmanpos[batsmanlist[0]]=0
    batsmanpos[batsmanlist[1]]=1
    count=1
    for i in innings1.iterrows():
        if i[1]['is_wicket']==1:
            count=count+1
            batsmanpos[batsmanlist[count]]=count
    print(batsmanpos)
