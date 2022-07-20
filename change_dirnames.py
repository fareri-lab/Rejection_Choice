#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:27:07 2022

@author: anthonyr1720
"""

import os

# path = os.getcwd()
sub_id = input("Enter subject id:")
expdir = os.getcwd()
subjdir = '%s/%s' % (expdir, subj_id)
if not os.path.exists(subjdir):
   os.makedirs(subjdir)
   
   


# Function to rename multiple files
def main():
   
    folder = os.getcwd() + '/Images/Participant_Images'
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"%s_image_{str(count)}.jpg" %(sub_id)
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()