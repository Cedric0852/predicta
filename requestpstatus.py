import requests
import json
import streamlit as st
###
#making api call 
params = {
  "api_key": "{api_key}",
  "offset": "0",
  "include_options": "0"
}
# Requesting project status
def requeststatus(data):
    r = requests.get('{pro_url}',params=params)
    return r.text
   
def data1(data1):
    data=requeststatus(requeststatus)
    jdat=json.loads(data)
    return jdat
@st.cache
def projecttoken(token):
    pt=data1(data1)["token"]
    return pt