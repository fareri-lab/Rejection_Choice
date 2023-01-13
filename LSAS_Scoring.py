#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:47:02 2023

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

# %%
#columns list
LSAS_avoidancecols = [col for col in alldata.columns if 'LSAS_1_' in col]
LSAS_fearcols = [col for col in alldata.columns if 'LSAS_2_' in col]
ProlificID_cols = [col for col in alldata.columns if 'post_task' in col]


LSAS = alldata.filter(regex='LSAS_|post_task')


# %%
LSAS_clean = pd.DataFrame()


for i in range(0, len(LSAS)):
    if LSAS.loc[i,'post_task'] in participants['PROLIFIC_ID'].values:
       LSAS_clean[i] = LSAS.loc[i]    

finaldata = pd.DataFrame()


LSAS_clean = LSAS_clean.transpose()
LSAS_clean = LSAS_clean.reset_index()
finaldata['Prolific_ID'] = LSAS_clean['post_task']
LSAS_clean = LSAS_clean.drop(['index'], axis = 1)
LSAS_clean = LSAS_clean.drop(['post_task'], axis = 1)
LSAS_clean = LSAS_clean.replace(np.nan, 0)
#%%
LSAS_score = pd.DataFrame(columns = LSAS_clean.columns, index = LSAS_clean.index)

#%%
LSAS_avoidance = pd.DataFrame()
LSAS_avoidance['LSAS_1_1'] = LSAS_clean['LSAS_1_1']
LSAS_avoidance['LSAS_1_2'] = LSAS_clean['LSAS_1_2']
LSAS_avoidance['LSAS_1_3'] = LSAS_clean['LSAS_1_3']
LSAS_avoidance['LSAS_1_4'] = LSAS_clean['LSAS_1_4']
LSAS_avoidance['LSAS_1_5'] = LSAS_clean['LSAS_1_5']
LSAS_avoidance['LSAS_1_6'] = LSAS_clean['LSAS_1_6']
LSAS_avoidance['LSAS_1_7'] = LSAS_clean['LSAS_1_7']
LSAS_avoidance['LSAS_1_8'] = LSAS_clean['LSAS_1_8']
LSAS_avoidance['LSAS_1_9'] = LSAS_clean['LSAS_1_9']
LSAS_avoidance['LSAS_1_10'] = LSAS_clean['LSAS_1_10']
LSAS_avoidance['LSAS_1_11'] = LSAS_clean['LSAS_1_11']
LSAS_avoidance['LSAS_1_12'] = LSAS_clean['LSAS_1_12']
LSAS_avoidance['LSAS_1_13'] = LSAS_clean['LSAS_1_13']
LSAS_avoidance['LSAS_1_14'] = LSAS_clean['LSAS_1_14']
LSAS_avoidance['LSAS_1_15'] = LSAS_clean['LSAS_1_15']
LSAS_avoidance['LSAS_1_16'] = LSAS_clean['LSAS_1_16']
LSAS_avoidance['LSAS_1_17'] = LSAS_clean['LSAS_1_17']
LSAS_avoidance['LSAS_1_18'] = LSAS_clean['LSAS_1_18']
LSAS_avoidance['LSAS_1_19'] = LSAS_clean['LSAS_1_19']
LSAS_avoidance['LSAS_1_20'] = LSAS_clean['LSAS_1_20']
LSAS_avoidance['LSAS_1_21'] = LSAS_clean['LSAS_1_21']
LSAS_avoidance['LSAS_1_22'] = LSAS_clean['LSAS_1_22']
LSAS_avoidance['LSAS_1_23'] = LSAS_clean['LSAS_1_23']
LSAS_avoidance['LSAS_1_24'] = LSAS_clean['LSAS_1_24']

LSAS_avoidance= LSAS_avoidance.astype(int)

#%%
LSAS_fear = pd.DataFrame()
LSAS_fear['LSAS_2_1'] = LSAS_clean['LSAS_2_1']
LSAS_fear['LSAS_2_2'] = LSAS_clean['LSAS_2_2']
LSAS_fear['LSAS_2_3'] = LSAS_clean['LSAS_2_3']
LSAS_fear['LSAS_2_4'] = LSAS_clean['LSAS_2_4']
LSAS_fear['LSAS_2_5'] = LSAS_clean['LSAS_2_5']
LSAS_fear['LSAS_2_6'] = LSAS_clean['LSAS_2_6']
LSAS_fear['LSAS_2_7'] = LSAS_clean['LSAS_2_7']
LSAS_fear['LSAS_2_8'] = LSAS_clean['LSAS_2_8']
LSAS_fear['LSAS_2_9'] = LSAS_clean['LSAS_2_9']
LSAS_fear['LSAS_2_10'] = LSAS_clean['LSAS_2_10']
LSAS_fear['LSAS_2_11'] = LSAS_clean['LSAS_2_11']
LSAS_fear['LSAS_2_12'] = LSAS_clean['LSAS_2_12']
LSAS_fear['LSAS_2_13'] = LSAS_clean['LSAS_2_13']
LSAS_fear['LSAS_2_14'] = LSAS_clean['LSAS_2_14']
LSAS_fear['LSAS_2_15'] = LSAS_clean['LSAS_2_15']
LSAS_fear['LSAS_2_16'] = LSAS_clean['LSAS_2_16']
LSAS_fear['LSAS_2_17'] = LSAS_clean['LSAS_2_17']
LSAS_fear['LSAS_2_18'] = LSAS_clean['LSAS_2_18']
LSAS_fear['LSAS_2_19'] = LSAS_clean['LSAS_2_19']
LSAS_fear['LSAS_2_20'] = LSAS_clean['LSAS_2_20']
LSAS_fear['LSAS_2_21'] = LSAS_clean['LSAS_2_21']
LSAS_fear['LSAS_2_22'] = LSAS_clean['LSAS_2_22']
LSAS_fear['LSAS_2_23'] = LSAS_clean['LSAS_2_23']
LSAS_fear['LSAS_2_24'] = LSAS_clean['LSAS_2_24']

LSAS_fear= LSAS_fear.astype(int)

#%%
LSAS_score =  pd.concat([LSAS_fear, LSAS_avoidance], axis=1)
LSAS_score["LSAS_avoidance"] = LSAS_avoidance.sum(axis=1)
LSAS_score["LSAS_fear"] = LSAS_fear.sum(axis=1)
LSAS_score["LSAS_total"] = LSAS_score['LSAS_avoidance'] + LSAS_score['LSAS_fear']

#%%

selfreportdata = pd.read_csv('selfreportdata_master.csv')
selfreportdata['LSAS_avoidance'] = LSAS_score["LSAS_avoidance"]
selfreportdata['LSAS_fear'] = LSAS_score["LSAS_fear"]
selfreportdata['LSAS_total'] = LSAS_score["LSAS_total"]
selfreportdata.to_csv('selfreportdata_master.csv', index=False)