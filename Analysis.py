#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 18:13:33 2023

@author: jordansiegel
"""

import pandas as pd
import numpy as np
import os 
import statistics 
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import ttest_rel

#mport seaborn as sns
#import seaborn.objects as so

current_dir = os.getcwd()
alltaskdata = pd.read_csv('RejChoice_MasterData.csv')
taskdata = pd.read_csv('Taskdata_foranalysis.csv')
taskdata = taskdata.sort_values(by=['Prolific_id'])


#%%
#get avg reaction time for photo share & continue after lottery
photosharert = alltaskdata['sharenextphoto_keyrt']
photosharert = pd.DataFrame(photosharert).replace(np.nan, 0)
photosharert_mean = photosharert['sharenextphoto_keyrt'].mean()
photosharert_stdev = statistics.stdev(photosharert['sharenextphoto_keyrt'])
print(photosharert_mean)
print(photosharert_stdev)

lotteryrt = alltaskdata['resumeafterlottery_keysrt']
lotteryrt = pd.DataFrame(lotteryrt).replace(np.nan, 0)
lotteryrt_mean = lotteryrt['resumeafterlottery_keysrt'].mean()
lotteryrt_stdev =statistics.stdev(lotteryrt['resumeafterlottery_keysrt'])
print(lotteryrt_mean)
print(lotteryrt_stdev)

#%%
#find mean response time & stdev for choice across all participants
choicert = pd.DataFrame()
choicert = taskdata['choice_keysrt']
choicert = pd.DataFrame(choicert)
choicert['choice_keysrt'] = choicert['choice_keysrt'].replace(np.nan, 0)

choicert_mean = choicert['choice_keysrt'].mean()
print(choicert_mean)

choicert_stdev = statistics.stdev(choicert['choice_keysrt'])
print(choicert_stdev)

#%%
#self is set to 1, computer is set to 0

#overall proportion of times self was selected as a choice
choice = pd.DataFrame()
choice = taskdata['choiceresponse']
choice = pd.DataFrame(choice)
overallchoiceproportion = choice['choiceresponse'].mean()
overallchoice_std = choice['choiceresponse'].std()
print(overallchoiceproportion)
print(overallchoice_std)

#%%

#overall proportion of selecting self across conditions
#neutral = 0, rejection = 1, acceptance = 2
#make dataframe for calculation

choice['condition'] = taskdata['condition']
choice = pd.DataFrame(choice)
choice = choice.dropna()

#slice dataframe to include only rows where condition is neutral
neutralchoice = choice[choice['condition'] == 0]

#calculate mean on subsection of data
neutralchoice_mean = neutralchoice['choiceresponse'].mean()
neutralchoice_std = neutralchoice['choiceresponse'].std()
print(neutralchoice_mean)
print(neutralchoice_std)

#make subsection of dataframe
rejchoice = choice[choice['condition'] == 1]

#calculate mean on subsection of data
rejchoice_mean = rejchoice['choiceresponse'].mean()
rejchoice_std = rejchoice['choiceresponse'].std()
print(rejchoice_mean)
print(rejchoice_std)

#generate new dataframe with acceptance condition only
acceptancechoice = choice[choice['condition'] == 2]

#calculate mean based on acceptance condition only data frame
acceptancechoice_mean = acceptancechoice['choiceresponse'].mean()
acceptancechoice_std = acceptancechoice['choiceresponse'].std()                 
print(acceptancechoice_mean)
print(acceptancechoice_std)

#%%

#salience levels by condition

salience = pd.DataFrame(taskdata['salience'])
salience['condition'] = taskdata['condition']

#slice dataframe to include only rows where condition is neutral
neutralsalience = salience[salience['condition'] == 0]

#calculate mean salience scoress across neutral condition
neutralsalience_mean = neutralsalience['salience'].mean()
neutralsalience_std = neutralsalience['salience'].std() 
print(neutralsalience_mean)
print(neutralsalience_std)

#slice dataframe to include only rows where condition is rejection
rejsalience = salience[salience['condition'] == 1]

#calculate mean salience scores across rejection condition
rejsalience_mean = rejsalience['salience'].mean()
rejsalience_std = rejsalience['salience'].std()
print(rejsalience_mean)
print(rejsalience_std)

#slice dataframe to include only rows where condition is acceptance
accsalience = salience[salience['condition'] == 2]

#calculate mean salience scores across acceptance condition
accsalience_mean = accsalience['salience'].mean()
accsalience_std = accsalience['salience'].std()
print(accsalience_mean)
print(accsalience_std)

#%%

stress = pd.DataFrame(taskdata['stress'])
stress['condition'] = taskdata['condition']

#slice dataframe to include only rows where condition is neutral
neutralstress = stress[stress['condition'] == 0]

#calculate mean for stress by neutral
neutralstress_mean = neutralstress['stress'].mean()
neutralstress_std = neutralstress['stress'].std()
print(neutralstress_mean)
print(neutralstress_std)

#slice dataframe to include only rows where condition is rejection
rejstress = stress[stress['condition'] == 1]

#calculate mean for stress by rejection
rejstress_mean = rejstress['stress'].mean()
rejstress_std = rejstress['stress'].std()
print(rejstress_mean)
print(rejstress_std)
# print(rejstress_std)

#slice dataframe to include only rows where condition is acceptance
accstress = stress[stress['condition'] == 2]

#calculate mean for stress by acceptance
accstress_mean = accstress['stress'].mean()
accstress_std = accstress['stress'].std()
print(accstress_mean)
print(accstress_std)

#%%

#paired samples t-test for condition by choice
t_stat, p_value = ttest_rel(rejchoice['choiceresponse'],acceptancechoice['choiceresponse'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)

#%% paired samples t-test for condition by salience

t_stat, p_value = ttest_rel(rejsalience['salience'],accsalience['salience'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)

#%%

t_stat, p_value = ttest_rel(rejstress['stress'],accstress['stress'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)

#%%

#import participant list
path = Path(r"%s"%(os.getcwd()))
# read in participant list
current_dir = os.getcwd()
participants = pd.read_excel('%s/participantlist.xlsx'%(path))
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
participants = pd.DataFrame(data=participants['PROLIFIC_ID'])

#%%
#isolate columns necessary for generating graphing csv
condition_col = [col for col in taskdata.columns if 'condition' in col]
choice_col = [col for col in taskdata.columns if 'choiceresponse' in col]
salience_col = [col for col in taskdata.columns if 'salience' in col]
stress_col = [col for col in taskdata.columns if 'stress' in col]
ProlificID_cols = [col for col in taskdata.columns if 'Prolific_' in col]

#%%

