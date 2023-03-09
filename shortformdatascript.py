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
rej_df = pd.DataFrame(index=participants.index)
rej_df['prolific_id'] = ''
rej_df['choice'] = ''
rej_df['condition'] = ''
rej_df['salience'] = ''
rej_df['stress'] = ''


#%%

#make acceptance data frame
acc_df = pd.DataFrame()
acc_df['prolific_id'] = ''
acc_df['choice'] = ''
acc_df['condition'] = ''
acc_df['salience'] = ''
acc_df['stress'] = ''


#%%

#make neutral data frame
neu_df = pd.DataFrame()
neu_df['prolific_id'] = ''
neu_df['choice'] = ''
neu_df['condition'] = ''
neu_df['salience'] = ''
neu_df['stress'] = ''

#%%

participantdata = pd.read_csv('/users/jordansiegel/Documents/GitHub/Rejection_Choice/data/5a4636c92f91ec0001dcba07_RejTask_2022-11-21_17h24.19.149.csv')

#%%
participantdata['Condition'] = participantdata['Condition'].replace(np.nan,'Empty',regex = True)

#%%
for row in range(0,len(participantdata)):
    if participantdata['playlottery'][row] == 0 or  participantdata['playlottery'][row] == 1 or  participantdata['playlottery'][row] == 999:
        if row < 183:
            if participantdata.loc[row+1,'Condition']== 'Rej':
                participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Rej')
            elif participantdata.loc[row+1,'Condition']== 'Neutral':
                 participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Neutral')
            elif participantdata.loc[row+1,'Condition']== 'Acc':
                participantdata['Condition'][row] =  participantdata['Condition'][row].replace('Empty', 'Acc')
#%%

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
rejection_saliencemean = rejection_salience['salience_rating'].sum()/len(rejection_salience)
print(rejection_saliencemean)

rejection_salience = rejection_salience.reset_index(drop = True)
rej_df['salience'][0] = rejection_salience['salience'][0]

#%%

rejection_stress = pd.DataFrame()
rejection_stress['stress'] = rejcondition['stress_level']

rejection_stress= rejection_stress.replace('NAN', np.nan,regex = True)
rejection_stress = rejection_stress.dropna()

rejection_stress= rejection_stress.astype(int)
rejection_stressmean = rejection_stress.mean()
print(rejection_stressmean)

#rej_df['stress'] = rejection_stressmean[0]

#%%
rejection_choice = pd.DataFrame()
rejection_choice['choice'] = rejcondition['playlottery']
rejection_choice = rejection_choice.dropna()
rejection_choice.drop(rejection_choice[(rejection_choice['choice'] == 999)].index, inplace = True)
rejection_choice = rejection_choice.reset_index(drop = True)

rejection_choicemean = rejection_choice.mean()
print(rejection_choicemean)

#rej_df['choice'] = rejection_choicemean[0]

#%%
#calculate mean salience rating across acceptance condition for one participant
acceptance_salience = pd.DataFrame()
acceptance_salience['salience_rating'] = acccondition['salience_rating']

#drop nans and empty spaces to make cumulative sum possible
acceptance_salience= acceptance_salience.replace('NAN', np.nan,regex = True)
acceptance_salience = acceptance_salience.dropna()

acceptance_salience= acceptance_salience.astype(int)
acceptance_saliencemean = acceptance_salience.mean()
print(acceptance_saliencemean)

#acc_df['salience'] = acceptance_saliencemean[0]

#%%

acceptance_stress = pd.DataFrame()
acceptance_stress['stress'] = acccondition['stress_level']

acceptance_stress= acceptance_stress.replace('NAN', np.nan,regex = True)
acceptance_stress = acceptance_stress.dropna()

acceptance_stress= acceptance_stress.astype(int)
acceptance_stressmean = acceptance_stress.mean()
print(acceptance_stressmean)

#acc_df['stress'] = acceptance_stressmean[0]

#%%

acceptance_choice = pd.DataFrame()
acceptance_choice['choice'] = acccondition['playlottery']
acceptance_choice = acceptance_choice.dropna()
acceptance_choice.drop(acceptance_choice[(acceptance_choice['choice'] == 999)].index, inplace = True)
acceptance_choice = acceptance_choice.reset_index(drop = True)

acceptance_choicemean = acceptance_choice.mean()
print(acceptance_choicemean)

#acc_df['choice'] = rejection_choicemean[0]

#%%
#calculate mean salience rating across neutral condition for one participant
neutral_salience = pd.DataFrame()
neutral_salience['salience_rating'] = neucondition['salience_rating']

#drop nans and empty spaces to make cumulative sum possible
neutral_salience= neutral_salience.replace('NAN', np.nan,regex = True)
neutral_salience = neutral_salience.dropna()

neutral_salience= neutral_salience.astype(int)
neutral_saliencemean = neutral_salience.mean()
print(neutral_saliencemean)

#neu_df['salience'] = neutral_saliencemean[0]

#%%

neutral_stress = pd.DataFrame()
neutral_stress['stress'] = neucondition['stress_level']

neutral_stress= neutral_stress.replace('NAN', np.nan,regex = True)
neutral_stress = neutral_stress.dropna()

neutral_stress= neutral_stress.astype(int)
neutral_stressmean = neutral_stress.mean()
print(neutral_stressmean)

#neu_df['stress'] = neutral_stressmean[0]

#%%

neutral_choice = pd.DataFrame()
neutral_choice['choice'] = neucondition['playlottery']
neutral_choice = neutral_choice.dropna()
neutral_choice.drop(neutral_choice[(neutral_choice['choice'] == 999)].index, inplace = True)
neutral_choice = neutral_choice.reset_index(drop = True)

neutral_choicemean = neutral_choice.mean()
print(neutral_choicemean)

#neu_df['choice'] = neutral_choicemean[0]