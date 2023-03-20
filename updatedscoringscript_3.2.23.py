#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:32:15 2023

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
import matplotlib.pyplot as plt

current_dir = os.getcwd()
updatedchoicedata = pd.read_csv('shortformdata.csv')

#%%

#indexing data frame to isolate variables by condition
neutralcondition = updatedchoicedata[updatedchoicedata['condition'] == 0]
rejectioncondition = updatedchoicedata[updatedchoicedata['condition'] == 1]
acceptcondition = updatedchoicedata[updatedchoicedata['condition'] == 2]

#%%

#proportion of self-choice in neutral condition
neutralchoice_mean = neutralcondition['choice'].mean()
neutralchoice_std = neutralcondition['choice'].std()
print('neutral_by_choice')
print(neutralchoice_mean)
print(neutralchoice_std)

#%%
#proportion of self-choice in rejection condition
rejectionchoice_mean = rejectioncondition['choice'].mean()
rejectionchoice_std = rejectioncondition['choice'].std()
print('rej_by_choice')
print(rejectionchoice_mean)
print(rejectionchoice_std)

#%%
#proportion of self-choice in acceptance condition
acceptchoice_mean = acceptcondition['choice'].mean()
acceptchoice_std = acceptcondition['choice'].std() 
print('acc_by_choice')                
print(acceptchoice_mean)
print(acceptchoice_std)

#%%

neutralsalience_mean = neutralcondition['salience'].mean()
neutralsalience_std = neutralcondition['salience'].std()
print('neutralsalience') 
print(neutralsalience_mean)
print(neutralsalience_std)

#%%

rejsalience_mean = rejectioncondition['salience'].mean()
rejsalience_std = rejectioncondition['salience'].std()
print('rejectionsalience')
print(rejsalience_mean)
print(rejsalience_std)

#%%

accsalience_mean = acceptcondition['salience'].mean()
accsalience_std = acceptcondition['salience'].std()
print('accsalience')
print(accsalience_mean)
print(accsalience_std)

#%%

neutralstress_mean = neutralcondition['stress'].mean()
neutralstress_std = neutralcondition['stress'].std()
print('neutralstress')
print(neutralstress_mean)
print(neutralstress_std)

#%%

rejstress_mean = rejectioncondition['stress'].mean()
rejstress_std = rejectioncondition['stress'].std()
print('rejstress')
print(rejstress_mean)
print(rejstress_std)

#%%

accstress_mean = acceptcondition['stress'].mean()
accstress_std = acceptcondition['stress'].std()
print('accstress')
print(accstress_mean)
print(accstress_std)

#%%
#paired samples t-test for condition by choice
t_stat, p_value = ttest_rel(rejectioncondition['choice'],acceptcondition['choice'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)

#%% paired samples t-test for condition by salience
t_stat, p_value = ttest_rel(rejectioncondition['salience'],acceptcondition['salience'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)

#%%
#paired samples t-test for condition by stress
t_stat, p_value = ttest_rel(rejectioncondition['stress'],acceptcondition['stress'])
print("T-statistic value:", t_stat)
print('P-value:', p_value)
#%%