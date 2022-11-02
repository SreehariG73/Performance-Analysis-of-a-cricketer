from typing import cast
from flask import Flask, render_template, jsonify, request, json
import pandas as pd
import numpy as np

import urllib.request
import json
def Pred(pname,bteam,venue):
    
    data = {
            "Inputs": {
                    "input1":
                    [
                        {
                                'id': "",   
                                'batsman': pname,   
                                'batsman_runs': "",   
                                'bowling_team': bteam,   
                                'Venue': venue,   
                        }
                    ],
            },
        "GlobalParameters":  {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/8679f19d5de949ff93358226eb1b0673/services/2c847056628b4bee9e658114f429b2fa/execute?api-version=2.0&format=swagger'
    api_key = 'Lfv1IdFmiKbir1aNxCIGtEL0Itlo07qAX9pwJhTR/r2TYn6MF+3q9OdocXKxcmB5CTNvNrzglWx8avJXFfHTOg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
        res = str(result)
        print(res[43:45])
        return res[43:45]
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))

#================================batsman analysis==============================
data=pd.read_csv('batsmandata.csv')

def vsteam(name):
    player=name
    playerdata=data[data['batsman']==player]
    bowlingteams=data['bowling_team'].unique()
    chartdata={}

    for i in bowlingteams:
        team_data=playerdata[playerdata['bowling_team']==i]
        chartdata[i]=int(team_data['batsman_runs'].sum())
    finalchartdata = []
    
    for team,run in chartdata.items():
        if run>0:
            finalchartdata.append({'Team':team,'Runs':run})
    #print(finalchartdata)
    return finalchartdata

def vsvenue(name):
    player=name
    playerdata=data[data['batsman']==player]
    venue=data['Venue'].unique()
    chartdata={}
    for i in venue:
        venue_data=playerdata[playerdata['Venue']==i]
        chartdata[i]=int(venue_data['batsman_runs'].sum())
    
    finalchartdata = []
    
    for v,run in chartdata.items():
        if run>0:
            finalchartdata.append({'Venue':v,'Runs':run})
    #print(finalchartdata)
    return finalchartdata

def innings(name):
    player=name
    playerdata=data[data['batsman']==player]
    innings1=playerdata[playerdata['Innings']==1]
    innings2=playerdata[playerdata['Innings']==2]
    i1runs=int(innings1['batsman_runs'].sum())
    i2runs=int(innings2['batsman_runs'].sum())
    print(i1runs,i2runs)
    idata=[{'innings':'1st Innings','Runs':i1runs},{'innings':'2nd Innings','Runs':i2runs}]
    return idata

def powerplay(name):
    player=name
    playerdata=data[data['batsman']==player]
    powerplay=int(playerdata['runs_in_powerplay'].sum())
    death=int(playerdata['runs_in_death'].sum())
    pdata=[{'over': 'powerplay','runs': powerplay},{'over': 'death','runs': death}]
    #print(pdata)
    return pdata

def bowling_type(name):
    player=name
    playerdata=data[data['batsman']==player]
    bowlingtype=playerdata['Bowler_Type'].unique()
    print(bowlingtype)
    bdata=[]
    for i in bowlingtype:
        btype=playerdata[playerdata['Bowler_Type']==i]
        gotout=int(btype['Bowler_Type'].count())
        bdata.append({'bowler type': i, 'Got out': gotout})
    print(bdata)
    return bdata

#=========================bowlers analysis=============================================
bowlers=pd.read_csv("bowlers.csv")

def bvsteams(name):
    bowlername=name
    bowlerdata=bowlers[bowlers['bowler']==bowlername]
    battingteams=bowlers['batting_team'].unique()
    chartdata={}

    for i in battingteams:
        team_data=bowlerdata[bowlerdata['batting_team']==i]
        chartdata[i]=int(team_data['wickets'].sum())
    finalchartdata = []
    
    for team,wickets in chartdata.items():
        if wickets>0:
            finalchartdata.append({'Team':team,'Wickets':wickets})
    print(finalchartdata)
    return finalchartdata

def bvsvenue(name):
    player=name
    playerdata=bowlers[bowlers['bowler']==player]
    venue=bowlers['venue'].unique()
    chartdata={}
    for i in venue:
        venue_data=playerdata[playerdata['venue']==i]
        chartdata[i]=int(venue_data['wickets'].sum())
    
    finalchartdata = []
    
    for v,wickets in chartdata.items():
        if wickets>0:
            finalchartdata.append({'Venue':v,'Wickets': wickets})
    #print(finalchartdata)
    return finalchartdata

#============================routing functions=============================
app = Flask(__name__)
import sqlite3 as sql

@app.route('/')
def hello_world():
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("select * from Teams")
    rows = cur.fetchall()
    return render_template('index.html',rows = rows)

@app.route('/analysis')
def analysis():
    return render_template('home.html')

@app.route('/ana',methods=['POST'])
def ana():
    pname = request.form['name']
    print(pname)
    return render_template('simple.html',name=pname)  

@app.route('/graph/<name>',methods=['GET','POST'])
def graph(name):
    pname = name
    return render_template('simple.html',name=pname)

@app.route('/data/<name>',methods=['GET','POST'])
def api_get_name(name): 
    # chartdata=
    # print(chartdata)
    return jsonify(vsteam(name))

@app.route('/pplay/<name>',methods=['GET','POST'])
def powerplay_api(name): 
    # chartdata=
    # print(chartdata)
    pdata=powerplay(name)
    return jsonify(pdata)    

@app.route('/vsvenue/<name>',methods=['GET','POST'])
def vsvenue_api(name):
    vdata=vsvenue(name)
    return jsonify(vdata)

@app.route('/innings/<name>',methods=['GET','POST'])
def innings_api(name):
    idata=innings(name)
    return jsonify(idata)

@app.route('/btype/<name>',methods=['GET','POST'])
def btype_api(name):
    bdata=bowling_type(name)
    return jsonify(bdata)

@app.route('/bvsteam/<name>',methods=['GET','POST'])
def bvsteam_api(name):
    bvsteamdata=bvsteams(name)
    print(bvsteamdata)
    return jsonify(bvsteamdata)

@app.route('/bvsvenue/<name>',methods=['GET','POST'])
def bvsvenue_api(name):
    bvsvenuedata=bvsvenue(name)
    print(bvsvenuedata)
    return jsonify(bvsvenuedata)

@app.route('/predict/<name>',methods=['GET','POST'])
def predict(name):
    pname = name
    return render_template('playerPred.html',name=pname)

@app.route('/predictPlayer',methods=['GET','POST'])
def predictPlayer():
    pname = request.form['fname']   
    bteam = request.form['bteam']
    venue = request.form['venue']
    val = Pred(pname,bteam,venue)
    print(pname,bteam,venue)
    return render_template('res.html',res = val,name = pname)



@app.route('/disPlayers/<name>',methods=['GET','POST'])
def disPlayers(name):
    print(name)
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("select * from {};".format(name))
    rows = cur.fetchall()
    
    return render_template('disPlayers.html',rows = rows)

if __name__ == '__main__':
   app.run(debug=True,port=8080)

