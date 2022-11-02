 
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'id': "",   
                            'batsman': "KL Rahul",   
                            'batsman_runs': "",   
                            'bowling_team': "Chennai Super Kings",   
                            'Venue': "M Chinnaswamy Stadium",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/8679f19d5de949ff93358226eb1b0673/services/d6ae320a81774ffeb1810b5840048462/execute?api-version=2.0&format=swagger'
api_key = 'LYmwVK+9iB9RxxybeH6qtMAbMfeEm+4NinWP6FECYsyOtBJmXWZuTy+uInvK8xKldH2/dIjVBO1AjnwUOzwnug==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'id': "",   
                            'batsman': "V Kohli",   
                            'batsman_runs': "",   
                            'bowling_team': "Kings XI Punjab",   
                            'Venue': "Punjab Cricket Association Stadium, Mohali",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/8679f19d5de949ff93358226eb1b0673/services/d6ae320a81774ffeb1810b5840048462/execute?api-version=2.0&format=swagger'
api_key = 'LYmwVK+9iB9RxxybeH6qtMAbMfeEm+4NinWP6FECYsyOtBJmXWZuTy+uInvK8xKldH2/dIjVBO1AjnwUOzwnug==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
