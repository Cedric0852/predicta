import requests
import json
import streamlit as st
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from dotenv.main import load_dotenv
from pathlib import Path
load_dotenv()
key=os.environ["api_key"]
status_url=os.environ["status_url"]


def requeststatus(data):
    r = requests.get(status_url+"="+key+"&offset=0&include_options=0")
    return r.text
   
def data1(data1):
    data=requeststatus(requeststatus)
    jdat=json.loads(data)
    return jdat
@st.cache
def projecttoken(token):
    pt=data1(data1)["token"]
    return pt