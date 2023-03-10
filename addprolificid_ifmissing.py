#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:49:17 2023

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
participants = pd.DataFrame( data= participants.sort_values().reset_index(drop=True))


data_path = '/Users/jordansiegel/Documents/GitHub/Rejection_Choice/data/'

for csv in os.listdir(data_path):
   for sub in range(0,len(participants)):
       if csv.startswith(participants['PROLIFIC_ID'][sub]):
           file = pd.read_csv(data_path+csv)
           file.insert(0,'PROLIFIC_ID',participants['PROLIFIC_ID'][sub])
           file.to_csv(data_path+csv, index=False)