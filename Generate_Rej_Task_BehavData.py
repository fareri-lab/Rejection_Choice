#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:42:10 2022

@author: melanieruiz
"""

import pandas as pd
import os 
#read in participant list
current_dir = os.getcwd()

participants = pd.read_excel('participantlist.xlsx')
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = participants['PROLIFIC_ID']

data = pd.DataFrame()


for k in range(0,(len(participants))):   #print(participants[k])
   for i in os.listdir(current_dir + '/data/'):
       if i.startswith(participants[k]) and i.endswith('.csv'):
           print(i)
           file = pd.read_csv('data/' + i)
           file = file.iloc[3:]
           columns_list = ['TrialNumber','Partner','Condition','Photos','Feedback','sharenextphoto_key.rt','choice_keys.keys','playlottery','choice_keys.rt','resumeafterlottery_keys.rt','salience_rating','stress_level']
           new_file = file[columns_list]
           new_file.insert(0,'PROLIFIC_ID', participants[k])
           #new_file= new_file.dropna()
           data = data.append(new_file, ignore_index=True)
         
            
            
            
data.to_csv('RejChoice_MasterData.csv', index=False)