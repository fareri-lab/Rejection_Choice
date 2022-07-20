#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 16:03:42 2022

@author: jordansiegel
"""
import itertools
import pandas as pd
import numpy as np
import random
from PIL import Image 
sociallevel = ["Rej", "Acc", "Neutral"]
partnerlist = ['Charlie', 'Sam', 'Riley']
condition = random.sample(sociallevel,3)
partner = ''
partner_selected = random.sample(partnerlist,3)
block = 0 #before experiment 
nTrials = 30

for i in range(0,3):
    if condition[i] == 'Rej':
        pDislike = .7
        pLike = .3
        partner = partner_selected[i]
        blocklist = ['disliked'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
        random.shuffle(blocklist)
        feedback = random.sample(blocklist,30)
        print(condition[i])
        print(partner)
        print(pDislike,pLike)
        print(block)
    elif condition[i] == 'Acc':
        pDislike = .3
        pLike = .7
        partner = partner_selected[i]
        blocklist = ['disliked'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
        random.shuffle(blocklist)
        feedback = random.sample(blocklist,30)
        print(condition[i])
        print(partner)
        print(pDislike,pLike)
        print(block)
    elif condition[i] == 'Neutral':
        pDislike = .5
        pLike = .5
        partner = partner_selected[i]
        blocklist = ['disliked'] * int(nTrials * pDislike) + ['liked'] * int(nTrials * pLike)
        random.shuffle(blocklist)
        feedback = random.sample(blocklist,30)
        print(condition[i])
        print(partner)
        print(pDislike,pLike)
        print(block)
    for trial in range (0,30):      
        feedbackresponses = ['%s %s your photo.' %(partner,feedback[trial])] 
        print('trial ' + condition[i])
        print('trial ' + partner)
        print(feedbackresponses)
    block = block+1
    
#should we just write the whole thing in code?
#displaying the first name and the first generated feedback, not iterating through all of them

        
        
       