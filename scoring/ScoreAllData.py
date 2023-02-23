#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:43:58 2023

@author: melanieruiz
"""

import pandas as pd
import os
from pathlib import Path


path = Path(r"%s"%(os.getcwd()))
phase = input('Pre? Post? or Both? ')

#import pre-surveys

if phase == 'Pre': 
    os.chdir('%s/Pre' %(path))
    import AQ_Scoring, BRCS_Scoring, ERQ_Scoring, NTBS_Scoring, PSS_Scoring, RSQ_Scoring, SCS_Scoring, SRQ_Scoring
elif phase == 'Post':
    os.chdir('%s/Post' %(path))
    import DAST_Scoring, DII_Scoring, LSAS_Scoring, MSPSS_Scoring, RR_Scoring
elif phase == 'Both':
    os.chdir('%s/Pre' %(path))
    import AQ_Scoring, BRCS_Scoring, ERQ_Scoring, NTBS_Scoring, PSS_Scoring, RSQ_Scoring, SCS_Scoring, SRQ_Scoring
    os.chdir('%s/Post' %(path))
    import DAST_Scoring, DII_Scoring, LSAS_Scoring, MSPSS_Scoring, RR_Scoring
else:
    print('Please enter Pre, Post, or Both')
# scoring_path = path + '/scoring/pre'


# if __name__ == "__main__":
#     for script in os.listdir(scoring_path):
#           if script.endswith('.py'):
#               os.system('python3 %s/%s' %(scoring_path,script))
