import requests
from requestpstatus import projecttoken
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from dotenv.main import load_dotenv
from pathlib import Path
load_dotenv()
key=os.environ["api_key"]
data_url=os.environ["data_url"]
data_url_2=os.environ["data_url_2"]
def getingcsv(csvdata):
    url= data_url+str(projecttoken(projecttoken))+data_url_2+"="+key+"&format=csv"   
    df=pd.read_csv(url,index_col=False) 
    return df

