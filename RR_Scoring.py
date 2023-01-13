#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:00:05 2023

@author: jordansiegel
"""
import pandas as pd
import os
import numpy as np

# read in participant list
current_dir = os.getcwd()
participants = pd.read_excel('participantlist.xlsx')
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = pd.DataFrame(data=participants['PROLIFIC_ID'])


#read in raw qualtrics data
alldata = pd.read_csv('RejectionChoice_PostTask.csv')
alldata = alldata.iloc[4:]
alldata = alldata.sort_values(by=['post_task'])
alldata.pop("Attnchk")  # remove attention checks
alldata = alldata.reset_index()
#%%

#columns list
RR_cols = [col for col in alldata.columns if 'RR_' in col]
ProlificID_cols = [col for col in alldata.columns if 'post_task' in col]

RR = alldata.filter(regex='RR_|post_task')

#%%
RR_clean = pd.DataFrame()


for i in range(0, len(RR)):
    if RR.loc[i,'post_task'] in participants['PROLIFIC_ID'].values:
       RR_clean[i] = RR.loc[i]    

finaldata = pd.DataFrame()


RR_clean = RR_clean.transpose()
RR_clean = RR_clean.reset_index()
finaldata['Prolific_ID'] = RR_clean['post_task']
RR_clean = RR_clean.drop(['index'], axis = 1)
RR_clean = RR_clean.drop(['post_task'], axis = 1)
RR_clean = RR_clean.replace(np.nan, 0)

#%%
RR_score = pd.DataFrame(columns = RR_clean.columns, index = RR_clean.index)

#%%
for k in range(0,len(RR_clean)):
    for i in range (0,len(RR_clean.columns)):
        RR_score[RR_clean.columns[i]][k] = RR_clean.loc[k,RR_clean.columns[i]]
        
RR_score= RR_score.astype(int)
RR_score["RR_totalscore"] = RR_score.sum(axis=1)

#%%
selfreportdata = pd.read_csv('selfreportdata_master.csv')
selfreportdata['RR'] = RR_score["RR_totalscore"]
selfreportdata.to_csv('selfreportdata_master.csv', index=False)

