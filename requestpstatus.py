import requests
import json
import streamlit as st
###
#making api call 
params = {
  "api_key": "tKp4tAsQ_yyi",
  "offset": "0",
  "include_options": "0"
}
# Requesting project status
def requeststatus(data):
    r = requests.get('https://www.parsehub.com/api/v2/projects/tV3pTmaTkwwL',params=params)
    return r.text
   
def data1(data1):
    data=requeststatus(requeststatus)
    jdat=json.loads(data)
    return jdat
@st.cache
def projecttoken(token):
    pt=data1(data1)["token"]
    return pt