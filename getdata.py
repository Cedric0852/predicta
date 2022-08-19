import requests
from requestpstatus import projecttoken
import streamlit as st
import pandas as pd
def getingcsv(csvdata):
    url= "https://www.parsehub.com/api/v2/projects/"+str(projecttoken(projecttoken))+"/last_ready_run/data?api_key=tKp4tAsQ_yyi&format=csv"   
    df=pd.read_csv(url,index_col=False) 
    return df
