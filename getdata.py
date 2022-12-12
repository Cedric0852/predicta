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
url1=os.environ["data_url"]
url2=os.environ["data_url_2"]
def getingcsv(csvdata):
    url= str(url1)+str(projecttoken(projecttoken))+str(url2)+"="+str(key)+"&format=csv"   
    df=pd.read_csv(url,index_col=False) 
    return df
