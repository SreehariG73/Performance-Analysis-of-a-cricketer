import pandas as pd
import numpy as np
import csv

data=pd.read_csv("D:/final year project/bowler.csv")
with open('bowlingtype.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["bowler","bowling_type"])
    bowlers=data['bowler'].unique()
    for i in bowlers:
        df=data[data['bowler']==i]
        bowlingtype=np.array(df['Bowler_Type'])
        writer.writerow([i,bowlingtype[0]])
