#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 5 12:27:50 2022

@author: Melanie Ruiz
"""

import os
import pandas as pd
import shutil


# read in raw qualtrics data and excel sheet of completed participants
# make csv into data frame
homedir = os.getcwd()
rawqualtrics = pd.read_csv('RejectionChoice_PhotoUpload3302023.csv')
current_subs = pd.read_excel('participantlist.xlsx')
current_subs = current_subs.loc[
    current_subs['filter_directory?'] == 'n']
current_subs = current_subs['PROLIFIC_ID'].reset_index(drop=True)
imagesfolder_path = os.getcwd() + '/Participant_Images/'
csvs_path = os.getcwd() + '/CSVs'
#%%

for i in os.listdir(imagesfolder_path):
    if not i.startswith('.DS_Store'):
        sub = i
        csvfile = '%s_trials.csv' %(i)
        src = os.path.join(imagesfolder_path + i, csvfile)
        dst = os.path.join(csvs_path, csvfile)
        shutil.copy(src, dst)
# %%
for i in os.listdir(imagesfolder_path):
    if not i in current_subs.values and not i.startswith('.DS_Store'):
        shutil.rmtree(os.path.join(imagesfolder_path,i))

#%%
