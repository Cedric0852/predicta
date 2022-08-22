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
def getingcsv(csvdata):
    url= "https://www.parsehub.com/api/v2/projects/"+str(projecttoken(projecttoken))+"/last_ready_run/data?api_key="+key+"&format=csv"   
    df=pd.read_csv(url,index_col=False) 
    return df

