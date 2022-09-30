#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 12:27:50 2022

@author: jordansiegel 
"""

import os
import pandas as pd
import itertools
import numpy as np
import random
from PIL import Image
import shutil
import fnmatch

#read in raw qualtrics data and excel sheet of completed participants
#make csv into data frame
rawqualtrics = pd.read_csv('qualtrics_data_8.4.csv')
completedparticipantlist = pd.read_excel('participantlist.xlsx')

#remove uneeded rows from data frame from raw qualtrics data
rawqualtrics = rawqualtrics.drop([0,1])

#reset index numbers for raw qualtrics dats
rawqualtrics = rawqualtrics.reset_index()

#gathering sub_ids of completed participants only
qualtrics = rawqualtrics.loc[rawqualtrics['ResponseId'].isin(completedparticipantlist['sub_id'])]
               
#%%
#setcurrentworking directory to a variable
expdir = os.getcwd()

image_dir =''
#make new folders for each participant and then a folder in each new folder
for i in range(0,len(qualtrics)):
    subj_id = qualtrics['ResponseId'][i]
    subj_dir = '%s/data/%s' % (expdir, subj_id)
    if os.path.exists (subj_dir):
        continue
    else:
        os.makedirs(subj_dir)
        image_dir = '%s/%s_Images' % (subj_dir,subj_id) 
        os.makedirs(image_dir)
        
    # if not os.path.exists (subj_dir):
    #     os.makedirs(subj_dir)
    # else:
    #     continue
    
    # image_dir = '%s/%s_Images' % (subj_dir,subj_id) 
    # if not os.path.exists (image_dir):
    #     os.makedirs(image_dir)
    # else:
    #     continue
#%%

source_folder = expdir + '/participant_images/'
qual_photo_folders = [f.path for f in os.scandir(source_folder) if f.is_dir()]
indv_image_folder = expdir + '/data/%s/%s_Images' 

for sub in qual_photo_folders:
    for f in os.listdir(sub):
        src = os.path.join(sub, f)
        dst = os.path.join(source_folder, f)
        shutil.move(src, dst)
for sub in qual_photo_folders:
        shutil.rmtree(sub)
for image in os.listdir(source_folder):
    for sub in range(0,len(qualtrics)):
        subj = (qualtrics['ResponseId'][sub])
        if len(os.listdir(indv_image_folder %(subj,subj))) == 30:
            continue
        else:
            if image.startswith(subj):
                src = os.path.join(source_folder , image)
                dst = os.path.join(indv_image_folder %(subj,subj),image)
                shutil.move(src, dst)
                
          
#creates variables to take files out of folders,move them to a different folder, and delete the original folders

#exceuting moving files from subfolders to a different folder and then deleting the old subfolders

#%%
# count increase by 1 in each iteration
# iterate all files from a directory
participantimagefolder = expdir + '/data/' 
count =1 
for p in os.listdir(participantimagefolder):
        if not p.endswith('.DS_Store'):
            if p.startswith('R_'):
                count = 1
                for photo in os.listdir(indv_image_folder %(p,p)):
                    if "_Image_" in photo:
                        continue
                    else:
                        if photo.endswith ('.jpg') or photo.endswith('.jpeg') or photo.endswith('.png'):
                            # Construct old file name
                            source = indv_image_folder%(p,p) + '/' + photo
                            # Adding the count to the new file name and extension
                            file_name, file_extension = os.path.splitext(photo)
                            
                            destination = indv_image_folder %(p,p) + '/' + p + "_Image_" + str(count) + ".jpeg"
                            # Renaming the file
                            os.rename(source, destination)
                            count += 1
     
                           
                                       
#%%
#for loop:
    #for x in
spreadsheet = pd.read_csv('spreadsheet_template.csv')
sociallevel = ["Rej", "Acc", "Neutral", "Acc","Rej"]
partnerlist = ['Charlie', 'Sam', 'Riley', 'Alex', 'Taylor']
condition = ''
partner = ''
feedback = ''


for folder in os.listdir(participantimagefolder):
    if not folder.endswith('.DS_Store'):
        imagedir = indv_image_folder %(folder,folder) +'/'
        os.chdir(imagedir)
        photolist = os.listdir(imagedir)
        photolist = [imagedir + x for x in photolist]
        condition_selected = random.sample(sociallevel,5)
        partner_selected = random.sample(partnerlist,5)
        block = 0 #before experiment
        nTrials = 30
        alltrials = pd.DataFrame(columns=['TrialNumber','Partner','Condition','Photos','Feedback', 'FeedbackWait'])
        alltrials['Partner'] = ''
        alltrials['Feedback'] = ''
        alltrials['Condition']= ''
        alltrials['Photos'] = ''
        # for k in range(0,len(photolist)):
        for i in range(0,5):
            if condition_selected[i] == 'Rej':
                pDislike = .7
                pLike = .3
                rej = pd.DataFrame(columns=['Partner','Condition','Photos','Feedback'])
                partner = partner_selected[i]
                condition = condition_selected[i]
                blocklist = ['did not like'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
                random.shuffle(blocklist)
                feedback = random.sample(blocklist,30)
                photo_selected = random.sample(photolist,30)
                rej['Feedback']=feedback
                rej['Partner']=partner
                rej['Condition']=condition
                rej['Photos']= photo_selected
                alltrials = pd.concat([alltrials, rej], ignore_index=True)
            elif condition_selected[i] == 'Acc':
                pDislike = .3
                pLike = .7
                acc = pd.DataFrame(columns=['Partner','Condition','Photos','Feedback'])
                partner = partner_selected[i]
                condition = condition_selected[i]
                blocklist = ['did not like'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
                random.shuffle(blocklist)
                feedback = random.sample(blocklist,30)
                photo_selected = random.sample(photolist,30)
                acc['Feedback']=feedback
                acc['Partner']=partner
                acc['Condition']=condition
                acc['Photos']= photo_selected
                alltrials = pd.concat([alltrials, acc], ignore_index=True)
            elif condition_selected[i] == 'Neutral':
                pDislike = .5
                pLike = .5
                neu = pd.DataFrame(columns=['Partner','Condition','Photos','Feedback'])
                partner = partner_selected[i]
                condition = condition_selected[i]
                blocklist = ['did not like'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
                random.shuffle(blocklist)
                feedback = random.sample(blocklist,30)
                photo_selected = random.sample(photolist,30)
                neu['Feedback']=feedback
                neu['Partner']=partner
                neu['Condition']=condition
                neu['Photos']= photo_selected
                alltrials = pd.concat([alltrials, neu], ignore_index=True)
        subid = folder
        expdir = participantimagefolder
        alltrials['FeedbackWait'] = spreadsheet['FeedbackWait']
        subjdir = '%s/%s' % (expdir, subid)
        trial_sheet = '%s/%s_trials.csv' %(subjdir,subid)
        alltrials['TrialNumber'] = range(1,len(alltrials)+1)
        alltrials.to_csv(trial_sheet, index= False)
    
