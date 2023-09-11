#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:31:24 2023

@author: jordansiegel
"""


from pathlib import Path
import pandas as pd 
import numpy as np
import os

#read in participant list
current_dir = os.getcwd()

participants_complete = pd.read_excel('participantlist.xlsx')

#toberecoded = participants.loc[participants['afterstresschange']== 0].reset_index(drop=True)
participants = participants_complete.loc[
    participants_complete['PhotosUploaded? (y/n)'] == 'y'].reset_index()
columns = ['PROLIFIC_ID']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))
participants_complete['order'] = ''
order = 0
#%%


for i in range(0,len(participants)):
    sub = participants['PROLIFIC_ID'][i]
    folder_path = 'Participant_Images/'
    sub_file = pd.read_csv(folder_path + sub +'/' + sub+ '_trials.csv')
    for trial in sub_file:
        if trial == 1:
            if sub_file['Condition'][trial] == 'Neutral':
                order = 0
            elif sub_file['Condition'][trial] == 'Rejection':
                order= 12
                
            elif sub_file['Condition'][trial] == 'Acceptance':
                order= 21
        if order > 1:
             break 
        else: 
             if trial == 30:
                if sub_file['Condition'][trial] == 'Neutral':
                     order = 0
                elif sub_file['Condition'][trial] == 'Rejection':
                     order= 12
                elif sub_file['Condition'][trial] == 'Acceptance':
                     order= 21    
             if order > 1:
                    break 
             else: 
                if trial == 60:
                    if sub_file['Condition'][trial] == 'Neutral':
                        order = 0
                    if sub_file['Condition'][trial] == 'Rejection':
                        order= 12
                    if sub_file['Condition'][trial] == 'Acceptance':
                        order= 21
        
        participants_complete['order'][sub] = order
