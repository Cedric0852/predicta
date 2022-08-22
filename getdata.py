import requests
from requestpstatus import projecttoken
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
def getingcsv(csvdata):
    url= "{url}"+str(projecttoken(projecttoken))+"/last_ready_run/data?api_key={api_key}&format=csv"   
    df=pd.read_csv(url,index_col=False) 
    return df
