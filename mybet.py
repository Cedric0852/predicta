from ipaddress import collapse_addresses
from unicodedata import name
import streamlit as st
import requests
import json
import csv
import pandas as pd
import os
import time
import datetime
import yagmail
import smtplib
import keyring
from requestpstatus import requeststatus ,data1 ,projecttoken
from getdata import getingcsv


#Proccesing and Sending Email
st.header("PREDICTA V1.2 ")
#sending email

if st.button("VIEW PREDICTION"):
    st.header("PREDICTION OF THE DAY")
    tote=getingcsv(getingcsv)
    tote.columns=['Country','League','Date','Team','Chance','Bet','Percentage']
    name=['Team','Chance','Bet','Percentage','Country','League','Date']
    tote.dropna()
    time.sleep(2)
    reteam=tote.reindex(columns=name)
    time.sleep(2)
    over85w=reteam[(reteam['Percentage'] >= "85")&(reteam['Chance'] == 'Winner')]
    #wining over 80% chance but under 85% AKA SILVER
    under85w=reteam[(reteam['Percentage'] <= "85")&(reteam['Percentage'] >= "80")&(reteam['Chance'] == 'Winner')]
    #double chance over 80% but Under 85% AKA PLATINUM
    under85dc=reteam[(reteam['Percentage'] <="85" )&(reteam['Percentage'] >="80" )&(reteam['Chance'] == 'Double Chance')]
    #Double chance over 85% chance AKA BRONZE
    over85dc=reteam[(reteam['Percentage'] >="85" )&(reteam['Chance'] == 'Double Chance')]
    #Wining over 85% chance AKA GOLD
    st.header("GOLD")
    st.write(" ")
    st.dataframe(over85w)
    st.write(" ")
    st.header("SILVER")
    st.write(" ")
    st.dataframe(under85w)
    st.write(" ")
    st.header("BRONZE")
    st.dataframe(over85dc)
    st.write(" ")
    st.header("PLATINUM")
    st.write(" ")
    st.dataframe(under85dc)
    st.write(" ")
    time.sleep(2)
    st.success("Predictions ready Good luck")
    st.info("BE RESPONSIBLE GAMBLE ,FOR EDUCATIONAL PURPOSES ONLY")
    st.balloons()
    
    