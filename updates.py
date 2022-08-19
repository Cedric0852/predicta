import requests
from runproject import runtoken
import json
#checking updates
def updates(stat):
    params3 = {
       "api_key": "tKp4tAsQ_yyi"
        }
    r3 = requests.get("https://www.parsehub.com/api/v2/runs/"+str(runtoken(runtoken)), params=params3)
    return r3.text

def updata(data):
    data3=updates(updates)
    jdata3=json.loads(data3)
    return jdata3

