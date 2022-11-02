import csv
import pandas as pd
import numpy as np
df=pd.read_csv("D:/final year project/IPL Ball-by-Ball 2008-2020.csv")
match=pd.read_csv("D:/final year project/matches.csv")
df=df.fillna(0)
match=match.fillna(0)
ids=df['id'].unique()
with open('batsmandata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id","batsman","batsman_runs","bowling_team","Venue","runs_in_powerplay","runs_in_death","Innings","Bowler"])
    for id in ids:
        df1=df.loc[(df['id']==id)]
        innings1=df1.loc[df1['inning']==1]
        innings2=df1.loc[df1['inning']==2]
        count=0
        m1=match.loc[(match['id']==id)]
        venue=np.array(m1['venue'])
        batsmanlist=df1['batsman'].unique()
        for b in batsmanlist:
            df2=df1.loc[df1['batsman']==b]
            powerplay=df2.loc[df2['over']<6]
            p_runs=powerplay['batsman_runs'].sum()
            death=df2.loc[df2['over']>14]
            d_runs=death['batsman_runs'].sum()
            runs=df2['batsman_runs'].sum()
            bowling_team=df2['bowling_team'].unique()
            innings=df2['inning'].unique()
            wicket=df2[df2['player_dismissed']==b]
            bowler=[""]
            if(not(wicket.empty)):
                if(not(wicket['dismissal_kind'].equals("run out"))):
                    bowler[0]=np.array(wicket['bowler'])
                else:
                    bowler[0]=np.array(wicket['dismissal_kind'])
            else:
                bowler[0]=np.array(["not out"])
            writer.writerow([id,b,runs,bowling_team[0],venue[0],p_runs,d_runs,innings[0],bowler[0][0]])
    
