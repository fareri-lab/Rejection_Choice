#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 12:02:31 2024

@author: jordansiegel
"""


from pathlib import Path
import pandas as pd 
import numpy as np
import os

#read in participant list
current_dir = os.getcwd()

participants = pd.read_excel('participantlist.xlsx')

#toberecoded = participants.loc[participants['afterstresschange']== 0].reset_index(drop=True)
participants = participants.loc[
    participants['PhotosUploaded? (y/n)'] == 'y'].reset_index()
columns = ['PROLIFIC_ID']
participants =participants[columns]
participants = pd.DataFrame(data = participants.sort_values(by='PROLIFIC_ID').reset_index(drop=True))

#%%


path = Path(r"%s"%(os.getcwd()))
p = Path('%s/data' %(path))
exploratory_cols = ['PROLIFIC_ID', 'choice', 'condition', 'condition_recode', 'trialnumber', 'feedback_words', 'feedbackvalue', 'overall_subblock_feedback']
exploratory_data= pd.DataFrame(columns = exploratory_cols)
#%%
#exploratory_df = pd.DataFrame(index=participants.index, columns = exploratory_cols)


data_path = os.getcwd()+'/data/'


# Define the data path
data_path = os.path.join(os.getcwd(), 'data')

# Initialize the final DataFrame
exploratory_df = pd.DataFrame()

# Iterate through each CSV file in the data directory
for csv in sorted(os.listdir(data_path)):
    # Iterate through each participant in the participants DataFrame
    for sub in range(len(participants)):
        # Check if the CSV file starts with the PROLIFIC_ID of the current participant
        if csv.startswith(participants['PROLIFIC_ID'][sub]):
            # Read the CSV file into a DataFrame
            participantdata = pd.read_csv(os.path.join(data_path, csv))
            
            # Ensure 'PROLIFIC_ID' column exists in participantdata
            if 'PROLIFIC_ID' not in participantdata.columns:
                participantdata['PROLIFIC_ID'] = participants['PROLIFIC_ID'][sub]
            else:
                participantdata['PROLIFIC_ID'] = participantdata['PROLIFIC_ID'].fillna(participants['PROLIFIC_ID'][sub])
            
            # Prepare a DataFrame for the current participant's data
            participantdata = pd.DataFrame({
                'PROLIFIC_ID': participants['PROLIFIC_ID'][sub],
                'trialnumber': participantdata['TrialNumber'].replace(np.nan, 'remove'),
                'choice': participantdata['playlottery'],
                'condition': participantdata['Condition'].replace(np.nan, 'remove'),
                'feedback_words': participantdata['Feedback'].replace(np.nan, 'remove')
            })
            
            # Append the current participant's data to the main DataFrame
            exploratory_df = pd.concat([exploratory_df, participantdata], ignore_index=True)
            
            #fill in choice column for trials 1-5 with the correct value
                
            if exploratory_df.at[7,'choice'] == 999:
                exploratory_df.loc[[6,5,4,3,8],'choice']= 999
            elif exploratory_df.at[7,'choice'] == 1:
                exploratory_df.loc[[6,5,4,3,8],'choice']= 1
            elif exploratory_df.at[7,'choice'] == 0:
                exploratory_df.loc[[6,5,4,3,8],'choice']= 0
                    
            #fill in choice column for trials 6-10 with the correct value
            
            if exploratory_df.at[13,'choice'] == 999:
                exploratory_df.loc[[9,10,11,12,14],'choice']= 999
            elif exploratory_df.at[13,'choice'] == 1:
                exploratory_df.loc[[9,10,11,12,14],'choice']= 1
            elif exploratory_df.at[13,'choice'] == 0:
                exploratory_df.loc[[9,10,11,12,14],'choice']= 0
                
            #trials 11-15
                
            if exploratory_df.at[19,'choice'] == 999:
                exploratory_df.loc[[15,16,17,18,20],'choice']= 999
            elif exploratory_df.at[19,'choice'] == 1:
                exploratory_df.loc[[15,16,17,18,20],'choice']= 1
            elif exploratory_df.at[19,'choice'] == 0:
                exploratory_df.loc[[15,16,17,18,20],'choice']= 0
                
            #trials 16-20   
            
            if exploratory_df.at[25,'choice'] == 999:
                exploratory_df.loc[[21,22,23,24,26],'choice']= 999
            elif exploratory_df.at[25,'choice'] == 1:
                exploratory_df.loc[[21,22,23,24,26],'choice']= 1
            elif exploratory_df.at[25,'choice'] == 0:
                exploratory_df.loc[[21,22,23,24,26],'choice']= 0
                
             #trials 21-25 
             
            if exploratory_df.at[31,'choice'] == 999:
                exploratory_df.loc[[27,28,29,30,32],'choice']= 999
            elif exploratory_df.at[31,'choice'] == 1:
                exploratory_df.loc[[27,28,29,30,32],'choice']= 1
            elif exploratory_df.at[31,'choice'] == 0:
                exploratory_df.loc[[27,28,29,30,32],'choice']= 0
                 
             #trials 26-30 
             
            if exploratory_df.at[37,'choice'] == 999:
                exploratory_df.loc[[33,34,35,36,38],'choice']= 999
            elif exploratory_df.at[37,'choice'] == 1:
                exploratory_df.loc[[33,34,35,36,38],'choice']= 1
            elif exploratory_df.at[37,'choice'] == 0:
                exploratory_df.loc[[33,34,35,36,38],'choice']= 0
            
            #trials 31-35 
            
            if exploratory_df.at[43,'choice'] == 999:
                exploratory_df.loc[[39,40,41,42,44],'choice']= 999
            elif exploratory_df.at[43,'choice'] == 1:
                exploratory_df.loc[[39,40,41,42,44],'choice']= 1
            elif exploratory_df.at[43,'choice'] == 0:
                exploratory_df.loc[[39,40,41,42,44],'choice']= 0
                
            #trials 36-40 
             
            if exploratory_df.at[49,'choice'] == 999:
                exploratory_df.loc[[45,46,47,48,50],'choice']= 999
            elif exploratory_df.at[49,'choice'] == 1:
                exploratory_df.loc[[45,46,47,48,50],'choice']= 1
            elif exploratory_df.at[31,'choice'] == 0:
                exploratory_df.loc[[45,46,47,48,50],'choice']= 0
            
            #trials 41-45 
            
            if exploratory_df.at[55,'choice'] == 999:
               exploratory_df.loc[[51,52,53,54,56],'choice']= 999
            elif exploratory_df.at[55,'choice'] == 1:
               exploratory_df.loc[[51,52,53,54,56],'choice']= 1
            elif exploratory_df.at[55,'choice'] == 0:
               exploratory_df.loc[[51,52,53,54,56],'choice']= 0
               
           #trials 46-50 
           
            if exploratory_df.at[61,'choice'] == 999:
              exploratory_df.loc[[57,58,59,60,62],'choice']= 999
            elif exploratory_df.at[61,'choice'] == 1:
              exploratory_df.loc[[57,58,59,60,62],'choice']= 1
            elif exploratory_df.at[61,'choice'] == 0:
              exploratory_df.loc[[57,58,59,60,62],'choice']= 0
              
            #trials 51-55 
            
            if exploratory_df.at[67,'choice'] == 999:
               exploratory_df.loc[[63,64,65,66,68],'choice']= 999
            elif exploratory_df.at[67,'choice'] == 1:
               exploratory_df.loc[[63,64,65,66,68],'choice']= 1
            elif exploratory_df.at[67,'choice'] == 0:
               exploratory_df.loc[[63,64,65,66,68],'choice']= 0
               
            #trials 56-60 
            
            if exploratory_df.at[73,'choice'] == 999:
               exploratory_df.loc[[69,70,71,72,74],'choice']= 999
            elif exploratory_df.at[73,'choice'] == 1:
               exploratory_df.loc[[69,70,71,72,74],'choice']= 1
            elif exploratory_df.at[73,'choice'] == 0:
               exploratory_df.loc[[69,70,71,72,74],'choice']= 0
               
             #trials 61-65 
             
            if exploratory_df.at[79,'choice'] == 999:
                exploratory_df.loc[[75,76,77,78,80],'choice']= 999
            elif exploratory_df.at[79,'choice'] == 1:
                exploratory_df.loc[[75,76,77,78,80],'choice']= 1
            elif exploratory_df.at[79,'choice'] == 0:
                exploratory_df.loc[[75,76,77,78,80],'choice']= 0
                
            #trials 66-70 
            
            if exploratory_df.at[85,'choice'] == 999:
               exploratory_df.loc[[81,82,83,84,86],'choice']= 999
            elif exploratory_df.at[85,'choice'] == 1:
               exploratory_df.loc[[81,82,83,84,86],'choice']= 1
            elif exploratory_df.at[85,'choice'] == 0:
               exploratory_df.loc[[81,82,83,84,86],'choice']= 0
               
             #trials 76-80 
             
            if exploratory_df.at[91,'choice'] == 999:
                exploratory_df.loc[[87,88,89,90,92],'choice']= 999
            elif exploratory_df.at[91,'choice'] == 1:
                exploratory_df.loc[[87,88,89,90,92],'choice']= 1
            elif exploratory_df.at[91,'choice'] == 0:
                exploratory_df.loc[[87,88,89,90,92],'choice']= 0
                
            #trials 81-85 
            
            if exploratory_df.at[97,'choice'] == 999:
               exploratory_df.loc[[93,94,95,96,98],'choice']= 999
            elif exploratory_df.at[97,'choice'] == 1:
               exploratory_df.loc[[93,94,95,96,98],'choice']= 1
            elif exploratory_df.at[97,'choice'] == 0:
               exploratory_df.loc[[93,94,95,96,98],'choice']= 0
               
             #trials 86-90 
             
            if exploratory_df.at[103,'choice'] == 999:
                exploratory_df.loc[[99,100,101,102,104],'choice']= 999
            elif exploratory_df.at[103,'choice'] == 1:
                exploratory_df.loc[[99,100,101,102,104],'choice']= 1
            elif exploratory_df.at[31,'choice'] == 0:
                exploratory_df.loc[[99,100,101,102,104],'choice']= 0
                
            #trials 91-95 
            
            if exploratory_df.at[109,'choice'] == 999:
               exploratory_df.loc[[105,106,107,108,110],'choice']= 999
            elif exploratory_df.at[109,'choice'] == 1:
               exploratory_df.loc[[105,106,107,108,110],'choice']= 1
            elif exploratory_df.at[109,'choice'] == 0:
               exploratory_df.loc[[105,106,107,108,110],'choice']= 0
               
             #trials 96-100 
             
            if exploratory_df.at[115,'choice'] == 999:
                exploratory_df.loc[[111,112,113,114,116],'choice']= 999
            elif exploratory_df.at[115,'choice'] == 1:
                exploratory_df.loc[[111,112,113,114,116],'choice']= 1
            elif exploratory_df.at[115,'choice'] == 0:
                exploratory_df.loc[[111,112,113,114,116],'choice']= 0
                
            #trials 101-105 
            
            if exploratory_df.at[121,'choice'] == 999:
               exploratory_df.loc[[117,118,119,120,122],'choice']= 999
            elif exploratory_df.at[121,'choice'] == 1:
               exploratory_df.loc[[117,118,119,120,122],'choice']= 1
            elif exploratory_df.at[121,'choice'] == 0:
               exploratory_df.loc[[117,118,119,120,122],'choice']= 0
               
             #trials 106-110 
              
            if exploratory_df.at[127,'choice'] == 999:
                 exploratory_df.loc[[123,124,125,126,128],'choice']= 999
            elif exploratory_df.at[127,'choice'] == 1:
                 exploratory_df.loc[[123,124,125,126,128],'choice']= 1
            elif exploratory_df.at[127,'choice'] == 0:
                 exploratory_df.loc[[123,124,125,126,128],'choice']= 0
                 
            #trials 111-115 
            
            if exploratory_df.at[133,'choice'] == 999:
               exploratory_df.loc[[129,130,131,132,134],'choice']= 999
            elif exploratory_df.at[133,'choice'] == 1:
               exploratory_df.loc[[129,130,131,132,134],'choice']= 1
            elif exploratory_df.at[133,'choice'] == 0:
               exploratory_df.loc[[129,130,131,132,134],'choice']= 0
               
              #trials 116-120
              
            if exploratory_df.at[139,'choice'] == 999:
                 exploratory_df.loc[[135,136,137,138,140],'choice']= 999
            elif exploratory_df.at[139,'choice'] == 1:
                 exploratory_df.loc[[135,136,137,138,140],'choice']= 1
            elif exploratory_df.at[139,'choice'] == 0:
                 exploratory_df.loc[[135,136,137,138,140],'choice']= 0
                 
            #trials 121-125 
            
            if exploratory_df.at[145,'choice'] == 999:
               exploratory_df.loc[[141,142,143,144,146],'choice']= 999
            elif exploratory_df.at[145,'choice'] == 1:
               exploratory_df.loc[[141,142,143,144,146],'choice']= 1
            elif exploratory_df.at[31,'choice'] == 0:
               exploratory_df.loc[[141,142,143,144,146],'choice']= 0
               
             #trials 126-130 
             
            if exploratory_df.at[151,'choice'] == 999:
                exploratory_df.loc[[147,148,149,150,152],'choice']= 999
            elif exploratory_df.at[151,'choice'] == 1:
                exploratory_df.loc[[147,148,149,150,152],'choice']= 1
            elif exploratory_df.at[151,'choice'] == 0:
                exploratory_df.loc[[147,148,149,150,152],'choice']= 0
                
             #trials 131-135 
             
            if exploratory_df.at[157,'choice'] == 999:
                exploratory_df.loc[[153,154,155,156,158],'choice']= 999
            elif exploratory_df.at[157,'choice'] == 1:
                exploratory_df.loc[[153,154,155,156,158],'choice']= 1
            elif exploratory_df.at[157,'choice'] == 0:
                exploratory_df.loc[[153,154,155,156,158],'choice']= 0
                
             #trials 136-140 
             
            if exploratory_df.at[163,'choice'] == 999:
                exploratory_df.loc[[159,160,161,162,164],'choice']= 999
            elif exploratory_df.at[163,'choice'] == 1:
                exploratory_df.loc[[159,160,161,162,164],'choice']= 1
            elif exploratory_df.at[163,'choice'] == 0:
                exploratory_df.loc[[159,160,161,162,164],'choice']= 0
                
            #trials141-145 
            
            if exploratory_df.at[169,'choice'] == 999:
               exploratory_df.loc[[165,166,167,168,170],'choice']= 999
            elif exploratory_df.at[169,'choice'] == 1:
               exploratory_df.loc[[165,166,167,168,170],'choice']= 1
            elif exploratory_df.at[169,'choice'] == 0:
               exploratory_df.loc[[165,166,167,168,170],'choice']= 0
               
              #trials 146-150
              
            if exploratory_df.at[175,'choice'] == 999:
                 exploratory_df.loc[[171,172,173,174,176],'choice']= 999
            elif exploratory_df.at[175,'choice'] == 1:
                 exploratory_df.loc[[171,172,173,174,176],'choice']= 1
            elif exploratory_df.at[175,'choice'] == 0:
                 exploratory_df.loc[[171,172,173,174,176],'choice']= 0
                 
            if exploratory_df.at[181,'choice'] == 999:
                 exploratory_df.loc[[177,178,179,180,182],'choice']= 999
            elif exploratory_df.at[181,'choice'] == 1:
                 exploratory_df.loc[[177,178,179,180,182],'choice']= 1
            elif exploratory_df.at[181,'choice'] == 0:
                 exploratory_df.loc[[177,178,179,180,182],'choice']= 0
            
            remove = 'remove'
            exploratorydf_cleaned = exploratory_df[exploratory_df['trialnumber'] != remove]
            exploratorydf_cleaned.reset_index(drop=True, inplace=True)
            
            
#%%            
exploratorydf_cleaned['condition_recode']=''            
exploratorydf_cleaned['feedbackvalue']='' 
exploratorydf_cleaned['overall_feedbackvalue']=''               


exploratorydf_cleaned.to_csv('exploratorydf_cleaned.csv', index=False)                   

  
              
        
                
            
                 
            
                
                
                
        