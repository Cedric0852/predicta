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
from runproject import runprojectonclick ,data2 ,runtoken
from cancelrun import canselproject ,cdata
from updates import updates ,updata
from getdata import getingcsv
#if button clicked get project status
if st.button("Get MYBET-V3.0 status",requeststatus):
    placeholder = st.empty()
    if not st.checkbox("Hide Status"):
        #converting data to json format
        jdata=data1(data1)
        #displaying data to webapp 
        st.title('Project Status')
        #selecting  and displaying specific element
        t=jdata["title"]
        '''Title :''', t
        #####################
        lrr=jdata['last_ready_run']["status"]
        '''Last Ready Run Status : ''' ,lrr
        ######################
        outtyp=jdata['output_type']
        '''Output Type : ''' ,outtyp
        #####################
        lrs=jdata["last_run"]["status"]
        '''Last run status : ''',lrs
        #########################
        stt=jdata["last_run"]["start_time"]
        ''' Start time : ''' ,stt
        ######################
        pag=jdata["last_run"]["pages"]
        '''Pages : ''',pag
        #####################
        endt=jdata["last_run"]["end_time"]
        '''End time : ''' ,endt
        #####################
        totr=jdata["total_runs"]
        '''Total Runs :''' ,totr
        #####################
        #defining project token
        '''Project Token : ''' ,projecttoken(projecttoken)
        ########Hiding data on check box
    else:
        placeholder.data()
##########
#Run project
if st.button("Run Project",runprojectonclick):
    placeholder = st.empty()
    if not st.checkbox("Hide Status"):
        jdata1=data2(data2)
        st.header("Run project Response")
        #########################
        '''Run Token : ''',runtoken(runtoken)
        ###########################
    else:
        placeholder.jdata1()

#######
##Cancel Project
if st.button("Cancel Run " ,canselproject):
    placeholder = st.empty()
    if not st.checkbox("Hide Status"):
        cdt=cdata(cdata)
        
        st.header("Canceled")
        #st.write(cdt)
        #################
        stus=cdt["run_token"]
        '''Status : ''' ,stus
    else:
        placeholder.cdt()
########
#Updates
if st.button("Status",updates):
        st.header("Project Run Status  ")
        #st.write(jdata3)
        #selecting imporanta paramenter
        ###################
        jdata3=updata(updata)
        ###########
        stu=jdata3["status"]
        ''' Status : ''',stu
        ##########################
        stime=jdata3["start_time"]
        '''Start time : ''',stime
        ##########################
        etime=jdata3["end_time"] 
        '''End Time :''',etime
        ##########################
        nump=jdata3["pages"]
        ''' Number of pages : ''',nump
        #########################
        runt=jdata3["run_token"]
        '''Run Token : ''',runt
        ###########################
        prot=jdata3["project_token"]
        '''Project Token  : ''',prot           
        ###########################
        dready=jdata3["data_ready"]
        '''Data ready : ''',dready
        #########################
        if stu == "complete":
            st.success("Completed Succeffuly")
            st.balloons()
        else:
            st.info("initialized")
##########
#Proccesing and Sending Email
if st.button("Proccess DATA"):
    st.header("Proccessing data")
    st.info("wait 15sec")
    tote=getingcsv(getingcsv)
    tote.columns=['Country','League','Date','Team','Chance','Bet','Percentage']
    time.sleep(2)
    reteam=tote.dropna()
    time.sleep(2)
    over85w=reteam[(reteam['Percentage'] >= "85")&(reteam['Chance'] == 'Winner')]
    #wining over 80% chance but under 85% AKA SILVER
    under85w=reteam[(reteam['Percentage'] <= "85")&(reteam['Percentage'] >= "80")&(reteam['Chance'] == 'Winner')]
    #double chance over 80% but Under 85% AKA PLATINUM
    under85dc=reteam[(reteam['Percentage'] <="85" )&(reteam['Percentage'] >="80" )&(reteam['Chance'] == 'Double Chance')]
    #Double chance over 85% chance AKA BRONZE
    over85dc=reteam[(reteam['Percentage'] >="85" )&(reteam['Chance'] == 'Double Chance')]
    #Printing FInal RESULT but only first 5 Team
    #EXPORT RESULT
    #EXPORT GOLD
    currentdate=datetime.datetime.today().strftime('%d-%b-%Y')
    over85w.to_csv('GOLD'+str(currentdate)+'.csv')
    time.sleep(3)
    #EXPORT SILVER
    under85w.to_csv('SILVA'+str(currentdate)+'.csv')
    time.sleep(3)
    #EXPORT BRONZE
    over85dc.to_csv('BRONZE(DC)'+str(currentdate)+'.csv')
    time.sleep(3)
    #EXPORT PLATINUM
    under85dc.to_csv('PLATINUM(DC)'+str(currentdate)+'.csv')
    time.sleep(3)
    #Both Teams To Score
    st.info("Proccessing data")
    time.sleep(2)
    st.success("Data is ready ")
#sending email
if st.button("VIEW DATA"):
    st.header("PREDICTION OF THE DAY")
    tote=getingcsv(getingcsv)
    tote.columns=['Country','League','Date','Team','Chance','Bet','Percentage']
    time.sleep(2)
    reteam=tote.dropna()
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
    
    