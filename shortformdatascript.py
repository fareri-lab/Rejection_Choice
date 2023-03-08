#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:57:05 2023

@author: jordansiegel
"""

from pathlib import Path
from collections import namedtuple
import pandas as pd 
import numpy as np
import os

#read in participant list
current_dir = os.getcwd()

participants = pd.read_excel('participantlist.xlsx')
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = participants['PROLIFIC_ID']

#%%

#read in csvs containing task data
shortformtaskdata = pd.read_csv('Updatedtaskdata_3.2.23.csv')
longformtaskdata = pd.read_csv('RejChoice_MasterData.csv')

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))

#%%

#make rejection data frame
rej_df = pd.DataFrame()
rej_df['prolific_id'] = ''
rej_df['propself_rej'] = ''
rej_df['condition'] = ''
rej_df['salience'] = ''
rej_df['stress'] = ''


#%%

#make acceptance data frame
acc_df = pd.DataFrame()
acc_df['prolific_id'] = ''
acc_df['propself_rej'] = ''
acc_df['condition'] = ''
acc_df['salience'] = ''
acc_df['stress'] = ''


#%%

#make neutral data frame
neu_df = pd.DataFrame()
neu_df['prolific_id'] = ''
neu_df['propself_rej'] = ''
neu_df['condition'] = ''
neu_df['salience'] = ''
neu_df['stress'] = ''

#%%

participantdata = pd.read_csv('/users/jordansiegel/Documents/GitHub/Rejection_Choice/data/5a4636c92f91ec0001dcba07_RejTask_2022-11-21_17h24.19.149.csv')
rejcondition = participantdata.loc[(participantdata['Condition'] == 'Rej')]
acccondition = participantdata.loc[(participantdata['Condition'] == 'Acc')]
neucondition = participantdata.loc[(participantdata['Condition'] == 'Neutral')]

rejcondition.insert(loc = 0,column = 'prolific_id',value = '5a4636c92f91ec0001dcba07')
acccondition.insert(loc = 0,column = 'prolific_id',value = '5a4636c92f91ec0001dcba07')
neucondition.insert(loc = 0,column = 'prolific_id',value = '5a4636c92f91ec0001dcba07')

#%%

#calculate mean salience rating across rejection condition for one participant
rejection_salience = pd.DataFrame()
rejection_salience['salience_rating'] = rejcondition['salience_rating']

#drop nans and empty spaces to make cumulative sum possible
rejection_salience= rejection_salience.replace('NAN', np.nan,regex = True)
rejection_salience = rejection_salience.dropna()

rejection_salience= rejection_salience.astype(int)
rejection_saliencemean = rejection_salience.mean()
print(rejection_saliencemean)

rej_df['salience'] = rejection_saliencemean[0]

#%%

rejection_stress = pd.DataFrame()
rejection_stress['stress'] = rejcondition['stress_level']

rejection_stress= rejection_stress.replace('NAN', np.nan,regex = True)
rejection_stress = rejection_stress.dropna()

rejection_stress= rejection_stress.astype(int)
rejection_stressmean = rejection_stress.mean()
print(rejection_stressmean)

rej_df['stress'] = rejection_stressmean[0]

#%%
for row in range(0,len(participantdata)):
    if participantdata['playlottery'][row] == 0 or  participantdata['playlottery'][row] == 1 or  participantdata['playlottery'][row] == 999:
        if participantdata.loc[row+1,'Condition']== 'Rej':
            participantdata['Condition'][row].replace(0, 'Rej' ,regex = True)

       