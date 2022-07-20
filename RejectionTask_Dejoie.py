#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon May  9 13:05:11 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard





# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'RejectionTask_Dejoie'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jordansiegel/Documents/PhD/Research/Second Year Project/Rejection_Task 2/RejectionTask_Dejoie.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome_Screen"
Welcome_ScreenClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text='Welcome to the Instagram Sharing Task!\n\n\n\n\n\n\n\nPress space to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "First_Instructions"
First_InstructionsClock = core.Clock()
FirstInstructions = visual.TextStim(win=win, name='FirstInstructions',
    text='To begin, you will be assigned a partner at random by the computer. \n\n\nNext, you will share your instagram photos with your partner. \n\n\nAfter sharing each photo, your partner will give you feedback on whether they liked or disliked your photo.',
    font='Open Sans',
    pos=(0, 0.08), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Block1_WaitingToMatch"
Block1_WaitingToMatchClock = core.Clock()
Match = visual.TextStim(win=win, name='Match',
    text='You will now be matched with a game partner selected at random by the computer.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
syncing = visual.TextStim(win=win, name='syncing',
    text='Syncing…',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Transparent = visual.Rect(
    win=win, name='Transparent',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.2,     colorSpace='rgb',  lineColor='white', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-2.0, interpolate=True)
Loading_25 = visual.Rect(
    win=win, name='Loading_25',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-0.375, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
text_25 = visual.TextStim(win=win, name='text_25',
    text='25%',
    font='Open Sans',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
Loading_50 = visual.Rect(
    win=win, name='Loading_50',
    width=(.5, 0.1)[0], height=(.5, 0.1)[1],
    ori=0.0, pos=(-0.25, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
text_50 = visual.TextStim(win=win, name='text_50',
    text='50%',
    font='Open Sans',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Loading_75 = visual.Rect(
    win=win, name='Loading_75',
    width=(0.75, 0.1)[0], height=(0.75, 0.1)[1],
    ori=0.0, pos=(-.125, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
text_75 = visual.TextStim(win=win, name='text_75',
    text='75%',
    font='Open Sans',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Loading_100 = visual.Rect(
    win=win, name='Loading_100',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
text_100 = visual.TextStim(win=win, name='text_100',
    text='100%',
    font='Open Sans',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Block1_Match"
Block1_MatchClock = core.Clock()
First_Match = visual.TextStim(win=win, name='First_Match',
    text='Your first match is Charlie!',
    font='Open Sans',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Images/sunglass emoji.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.25, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_3 = keyboard.Keyboard()
PressToContinue = visual.TextStim(win=win, name='PressToContinue',
    text='Press space to continue.',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Block1_Photo"
Block1_PhotoClock = core.Clock()
Photo_One = visual.TextStim(win=win, name='Photo_One',
    text='This photo will now be shared with Charlie.',
    font='Open Sans',
    pos=(0, .4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Image_One = visual.ImageStim(
    win=win,
    name='Image_One', 
    image='Images/Image_One.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='Please wait for feedback.',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block1_Waitingforfeedback"
Block1_WaitingforfeedbackClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Waiting…',
    font='Open Sans',
    pos=(0, 0.0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block1Feedback"
Block1FeedbackClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Block1_Fixation"
Block1_FixationClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press space to share your next photo.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Block1_Choice"
Block1_ChoiceClock = core.Clock()
lottery_game_choice = visual.TextStim(win=win, name='lottery_game_choice',
    text='You now have the option to play a lottery game!\n\n\nWould you like to play or have the computer play on your behalf? \n\nIf you chose to play, you will have 3 seconds to record your choice.\n',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
computer = visual.TextStim(win=win, name='computer',
    text='Computer',
    font='Open Sans',
    pos=(-.3, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
self_selected = visual.TextStim(win=win, name='self_selected',
    text='Self',
    font='Open Sans',
    pos=(0.3, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_4 = keyboard.Keyboard()
response_msg = ' '
feedback_msg = ' '
computer_choice = ['lower','higher']


# Initialize components for Routine "Block1_Lotterycomputerchoice"
Block1_LotterycomputerchoiceClock = core.Clock()
lotterycard = visual.TextStim(win=win, name='lotterycard',
    text='The computer will select whether it believes the card will be higher or lower than 5.',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Block1_facedowncard = visual.ImageStim(
    win=win,
    name='Block1_facedowncard', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
computerresponse = visual.TextStim(win=win, name='computerresponse',
    text='',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Block1_Lotteryselfchoice"
Block1_LotteryselfchoiceClock = core.Clock()
pickacard = visual.TextStim(win=win, name='pickacard',
    text='Please select whether you believe the card will be higher or lower than 5.',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
high = visual.TextStim(win=win, name='high',
    text='Higher',
    font='Open Sans',
    pos=(0.3, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
low = visual.TextStim(win=win, name='low',
    text='Lower',
    font='Open Sans',
    pos=(-.3, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()
responsefeedback = visual.TextStim(win=win, name='responsefeedback',
    text='',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
block1_cardimage = visual.ImageStim(
    win=win,
    name='block1_cardimage', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "Block2_WaitingMatch2"
Block2_WaitingMatch2Clock = core.Clock()
secondparnter = visual.TextStim(win=win, name='secondparnter',
    text='You will now be matched with a new partner.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
syncing2 = visual.TextStim(win=win, name='syncing2',
    text='Syncing…',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
polygon_2 = visual.Rect(
    win=win, name='polygon_2',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
loading_25 = visual.TextStim(win=win, name='loading_25',
    text='25%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
loading_1 = visual.Rect(
    win=win, name='loading_1',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-0.375, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
loading_50 = visual.TextStim(win=win, name='loading_50',
    text='50%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
loading_2 = visual.Rect(
    win=win, name='loading_2',
    width=(0.5, 0.1)[0], height=(0.5, 0.1)[1],
    ori=0.0, pos=(-.25, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
loading_75 = visual.TextStim(win=win, name='loading_75',
    text='75%',
    font='Open Sans',
    pos=(-.2, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
loading_3 = visual.Rect(
    win=win, name='loading_3',
    width=(0.75, 0.1)[0], height=(0.75, 0.1)[1],
    ori=0.0, pos=(-.125, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
loading_100 = visual.TextStim(win=win, name='loading_100',
    text='100%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
loading_full = visual.Rect(
    win=win, name='loading_full',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)

# Initialize components for Routine "Block2_Match"
Block2_MatchClock = core.Clock()
nerdface = visual.ImageStim(
    win=win,
    name='nerdface', 
    image='Images/nerd emoji.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_6 = keyboard.Keyboard()
Sam = visual.TextStim(win=win, name='Sam',
    text='You matched with Sam!\n\n\n\n\n\n\n\n\nPress space to continue.',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Block2_Photo"
Block2_PhotoClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='Images/Image_One.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text = visual.TextStim(win=win, name='text',
    text='This photo will now be shared with Sam. Please wait for feedback.',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block2_Waitingforfeedback"
Block2_WaitingforfeedbackClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Waiting…',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block2_Feedback"
Block2_FeedbackClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text=Response,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image=Graphic, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Block2_Fixation"
Block2_FixationClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Press space to share your next photo.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "Block2_choice"
Block2_choiceClock = core.Clock()
choice = visual.TextStim(win=win, name='choice',
    text='You will now have the option to play a lottery game!\n\n\n\n\nWould you like to play or have the computer play on your behalf?',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block2computer = visual.TextStim(win=win, name='block2computer',
    text='Computer',
    font='Open Sans',
    pos=(-0.3, -0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
self = visual.TextStim(win=win, name='self',
    text='self',
    font='Open Sans',
    pos=(0.3, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_7 = keyboard.Keyboard()
block2response_msg = ' '
block2feedback_msg = ' '
block2computer_choice = ['lower','higher']


# Initialize components for Routine "Block2_Lotterycomputerchoice"
Block2_LotterycomputerchoiceClock = core.Clock()
instruction = visual.TextStim(win=win, name='instruction',
    text='The computer will select whether it believes the card will be higher or lower than 7.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
computerresponse2 = visual.TextStim(win=win, name='computerresponse2',
    text=block2response_msg,
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
card = visual.ImageStim(
    win=win,
    name='card', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Block2_Lotteryselfchoice"
Block2_LotteryselfchoiceClock = core.Clock()
instructionsforselfchoice2 = visual.TextStim(win=win, name='instructionsforselfchoice2',
    text='Please select whether you believe the card will be higher or lower than 5.',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block2_higherchoice = visual.TextStim(win=win, name='block2_higherchoice',
    text='Higher',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block2_lowerchoice = visual.TextStim(win=win, name='block2_lowerchoice',
    text='Lower',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_8 = keyboard.Keyboard()
block2_responsefeedback = visual.TextStim(win=win, name='block2_responsefeedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);


block2_cardimage = visual.ImageStim(
    win=win,
    name='block2_cardimage', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "Block3_waitingtomatch"
Block3_waitingtomatchClock = core.Clock()
block3_match = visual.TextStim(win=win, name='block3_match',
    text='You will now be matched with a new partner.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
syncing3 = visual.TextStim(win=win, name='syncing3',
    text='Syncing…',
    font='Open Sans',
    pos=(0, 0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
polygon3 = visual.Rect(
    win=win, name='polygon3',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-2.0, interpolate=True)
loading25 = visual.TextStim(win=win, name='loading25',
    text='25%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
block3loading1 = visual.ShapeStim(
    win=win, name='block3loading1',
    size=(0.25, 0.1), vertices='triangle',
    ori=0.0, pos=(-0.375, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
loading50 = visual.TextStim(win=win, name='loading50',
    text='50%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
block3loading2 = visual.Rect(
    win=win, name='block3loading2',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-.25, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
loading75 = visual.TextStim(win=win, name='loading75',
    text='75%',
    font='Open Sans',
    pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
blockloading3 = visual.Rect(
    win=win, name='blockloading3',
    width=(0.75, 0.1)[0], height=(0.75, 0.1)[1],
    ori=0.0, pos=(-.125, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-8.0, interpolate=True)
loading100 = visual.TextStim(win=win, name='loading100',
    text='100%',
    font='Open Sans',
    pos=(0, -0.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
block3loadingfull = visual.Rect(
    win=win, name='block3loadingfull',
    width=(1, 0.1)[0], height=(1, 0.1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)

# Initialize components for Routine "Block3_Match"
Block3_MatchClock = core.Clock()
block3match = visual.TextStim(win=win, name='block3match',
    text='You have matched with Riley!\n\n\n\n\n\n\n\nPress space to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='Images/sillyemoji.webp', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Block3_Photo"
Block3_PhotoClock = core.Clock()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='Images/Image_One.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='This photo will now be shared with Riley. Please wait for feedback.',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Block3_Waitingforfeedback"
Block3_WaitingforfeedbackClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Waiting…',
    font='Open Sans',
    pos=(0, 0.4), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block3_feedback"
Block3_feedbackClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text=Response,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image=Graphic, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Block3_Fixation"
Block3_FixationClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Press space to share your next photo.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "Block3_Choice"
Block3_ChoiceClock = core.Clock()
block3response_msg = ' '
block3feedback_msg = ' '
block3computer_choice = ['lower','higher']

key_resp_13 = keyboard.Keyboard()
block3_choice = visual.TextStim(win=win, name='block3_choice',
    text='You will now have the option to play a lottery game!\n\n\n\n\nWould you like to play or have the computer play on your behalf?',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
block3_computer = visual.TextStim(win=win, name='block3_computer',
    text='Computer',
    font='Open Sans',
    pos=(-0.3, -0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
block3_self = visual.TextStim(win=win, name='block3_self',
    text='Self',
    font='Open Sans',
    pos=(0.3, -0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Block3_lotterycomputerchoice"
Block3_lotterycomputerchoiceClock = core.Clock()
Block3_lotcomputerchoice = visual.TextStim(win=win, name='Block3_lotcomputerchoice',
    text='The computer will select whether it believes the card will be higher or lower than 3.',
    font='Open Sans',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Block3_computerresponse = visual.TextStim(win=win, name='Block3_computerresponse',
    text=block3response_msg,
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
block3_cardimage = visual.ImageStim(
    win=win,
    name='block3_cardimage', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Block3_lotteryselfchoice"
Block3_lotteryselfchoiceClock = core.Clock()
block3_lotteryintstructions = visual.TextStim(win=win, name='block3_lotteryintstructions',
    text='Please select whether you believe the card will be higher or lower than 5.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
block3_higher = visual.TextStim(win=win, name='block3_higher',
    text='Higher',
    font='Open Sans',
    pos=(0.3, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
block3_lower = visual.TextStim(win=win, name='block3_lower',
    text='Lower',
    font='Open Sans',
    pos=(-.3, -.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_14 = keyboard.Keyboard()
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='Images/facedown card.jpeg', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
block3_feedbackresponse = visual.TextStim(win=win, name='block3_feedbackresponse',
    text=block3response_msg,
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome_Screen"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Welcome_ScreenComponents = [Welcome, key_resp]
for thisComponent in Welcome_ScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome_ScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome_Screen"-------
while continueRoutine:
    # get current time
    t = Welcome_ScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome_ScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome_Screen"-------
for thisComponent in Welcome_ScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "First_Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
First_InstructionsComponents = [FirstInstructions, key_resp_2]
for thisComponent in First_InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
First_InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "First_Instructions"-------
while continueRoutine:
    # get current time
    t = First_InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=First_InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FirstInstructions* updates
    if FirstInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FirstInstructions.frameNStart = frameN  # exact frame index
        FirstInstructions.tStart = t  # local t and not account for scr refresh
        FirstInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FirstInstructions, 'tStartRefresh')  # time at next scr refresh
        FirstInstructions.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in First_InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "First_Instructions"-------
for thisComponent in First_InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FirstInstructions.started', FirstInstructions.tStartRefresh)
thisExp.addData('FirstInstructions.stopped', FirstInstructions.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "First_Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Block1_WaitingToMatch"-------
continueRoutine = True
routineTimer.add(9.250000)
# update component parameters for each repeat
# keep track of which components have finished
Block1_WaitingToMatchComponents = [Match, syncing, Transparent, Loading_25, text_25, Loading_50, text_50, Loading_75, text_75, Loading_100, text_100]
for thisComponent in Block1_WaitingToMatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block1_WaitingToMatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block1_WaitingToMatch"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block1_WaitingToMatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block1_WaitingToMatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Match* updates
    if Match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Match.frameNStart = frameN  # exact frame index
        Match.tStart = t  # local t and not account for scr refresh
        Match.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Match, 'tStartRefresh')  # time at next scr refresh
        Match.setAutoDraw(True)
    if Match.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Match.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            Match.tStop = t  # not accounting for scr refresh
            Match.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Match, 'tStopRefresh')  # time at next scr refresh
            Match.setAutoDraw(False)
    
    # *syncing* updates
    if syncing.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        syncing.frameNStart = frameN  # exact frame index
        syncing.tStart = t  # local t and not account for scr refresh
        syncing.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(syncing, 'tStartRefresh')  # time at next scr refresh
        syncing.setAutoDraw(True)
    if syncing.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > syncing.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            syncing.tStop = t  # not accounting for scr refresh
            syncing.frameNStop = frameN  # exact frame index
            win.timeOnFlip(syncing, 'tStopRefresh')  # time at next scr refresh
            syncing.setAutoDraw(False)
    
    # *Transparent* updates
    if Transparent.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        Transparent.frameNStart = frameN  # exact frame index
        Transparent.tStart = t  # local t and not account for scr refresh
        Transparent.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Transparent, 'tStartRefresh')  # time at next scr refresh
        Transparent.setAutoDraw(True)
    if Transparent.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Transparent.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            Transparent.tStop = t  # not accounting for scr refresh
            Transparent.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Transparent, 'tStopRefresh')  # time at next scr refresh
            Transparent.setAutoDraw(False)
    
    # *Loading_25* updates
    if Loading_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        Loading_25.frameNStart = frameN  # exact frame index
        Loading_25.tStart = t  # local t and not account for scr refresh
        Loading_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Loading_25, 'tStartRefresh')  # time at next scr refresh
        Loading_25.setAutoDraw(True)
    if Loading_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Loading_25.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            Loading_25.tStop = t  # not accounting for scr refresh
            Loading_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Loading_25, 'tStopRefresh')  # time at next scr refresh
            Loading_25.setAutoDraw(False)
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    if text_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_25.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            text_25.tStop = t  # not accounting for scr refresh
            text_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
            text_25.setAutoDraw(False)
    
    # *Loading_50* updates
    if Loading_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        Loading_50.frameNStart = frameN  # exact frame index
        Loading_50.tStart = t  # local t and not account for scr refresh
        Loading_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Loading_50, 'tStartRefresh')  # time at next scr refresh
        Loading_50.setAutoDraw(True)
    if Loading_50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Loading_50.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            Loading_50.tStop = t  # not accounting for scr refresh
            Loading_50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Loading_50, 'tStopRefresh')  # time at next scr refresh
            Loading_50.setAutoDraw(False)
    
    # *text_50* updates
    if text_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        text_50.frameNStart = frameN  # exact frame index
        text_50.tStart = t  # local t and not account for scr refresh
        text_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        text_50.setAutoDraw(True)
    if text_50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_50.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            text_50.tStop = t  # not accounting for scr refresh
            text_50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_50, 'tStopRefresh')  # time at next scr refresh
            text_50.setAutoDraw(False)
    
    # *Loading_75* updates
    if Loading_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        Loading_75.frameNStart = frameN  # exact frame index
        Loading_75.tStart = t  # local t and not account for scr refresh
        Loading_75.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Loading_75, 'tStartRefresh')  # time at next scr refresh
        Loading_75.setAutoDraw(True)
    if Loading_75.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Loading_75.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            Loading_75.tStop = t  # not accounting for scr refresh
            Loading_75.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Loading_75, 'tStopRefresh')  # time at next scr refresh
            Loading_75.setAutoDraw(False)
    
    # *text_75* updates
    if text_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        text_75.frameNStart = frameN  # exact frame index
        text_75.tStart = t  # local t and not account for scr refresh
        text_75.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_75, 'tStartRefresh')  # time at next scr refresh
        text_75.setAutoDraw(True)
    if text_75.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_75.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            text_75.tStop = t  # not accounting for scr refresh
            text_75.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_75, 'tStopRefresh')  # time at next scr refresh
            text_75.setAutoDraw(False)
    
    # *Loading_100* updates
    if Loading_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        Loading_100.frameNStart = frameN  # exact frame index
        Loading_100.tStart = t  # local t and not account for scr refresh
        Loading_100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Loading_100, 'tStartRefresh')  # time at next scr refresh
        Loading_100.setAutoDraw(True)
    if Loading_100.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Loading_100.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            Loading_100.tStop = t  # not accounting for scr refresh
            Loading_100.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Loading_100, 'tStopRefresh')  # time at next scr refresh
            Loading_100.setAutoDraw(False)
    
    # *text_100* updates
    if text_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        text_100.frameNStart = frameN  # exact frame index
        text_100.tStart = t  # local t and not account for scr refresh
        text_100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_100, 'tStartRefresh')  # time at next scr refresh
        text_100.setAutoDraw(True)
    if text_100.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_100.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            text_100.tStop = t  # not accounting for scr refresh
            text_100.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_100, 'tStopRefresh')  # time at next scr refresh
            text_100.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block1_WaitingToMatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block1_WaitingToMatch"-------
for thisComponent in Block1_WaitingToMatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Match.started', Match.tStartRefresh)
thisExp.addData('Match.stopped', Match.tStopRefresh)
thisExp.addData('syncing.started', syncing.tStartRefresh)
thisExp.addData('syncing.stopped', syncing.tStopRefresh)
thisExp.addData('Transparent.started', Transparent.tStartRefresh)
thisExp.addData('Transparent.stopped', Transparent.tStopRefresh)
thisExp.addData('Loading_25.started', Loading_25.tStartRefresh)
thisExp.addData('Loading_25.stopped', Loading_25.tStopRefresh)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
thisExp.addData('Loading_50.started', Loading_50.tStartRefresh)
thisExp.addData('Loading_50.stopped', Loading_50.tStopRefresh)
thisExp.addData('text_50.started', text_50.tStartRefresh)
thisExp.addData('text_50.stopped', text_50.tStopRefresh)
thisExp.addData('Loading_75.started', Loading_75.tStartRefresh)
thisExp.addData('Loading_75.stopped', Loading_75.tStopRefresh)
thisExp.addData('text_75.started', text_75.tStartRefresh)
thisExp.addData('text_75.stopped', text_75.tStopRefresh)
thisExp.addData('Loading_100.started', Loading_100.tStartRefresh)
thisExp.addData('Loading_100.stopped', Loading_100.tStopRefresh)
thisExp.addData('text_100.started', text_100.tStartRefresh)
thisExp.addData('text_100.stopped', text_100.tStopRefresh)

# ------Prepare to start Routine "Block1_Match"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Block1_MatchComponents = [First_Match, image, key_resp_3, PressToContinue]
for thisComponent in Block1_MatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block1_MatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block1_Match"-------
while continueRoutine:
    # get current time
    t = Block1_MatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block1_MatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *First_Match* updates
    if First_Match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        First_Match.frameNStart = frameN  # exact frame index
        First_Match.tStart = t  # local t and not account for scr refresh
        First_Match.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(First_Match, 'tStartRefresh')  # time at next scr refresh
        First_Match.setAutoDraw(True)
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *PressToContinue* updates
    if PressToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        PressToContinue.frameNStart = frameN  # exact frame index
        PressToContinue.tStart = t  # local t and not account for scr refresh
        PressToContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(PressToContinue, 'tStartRefresh')  # time at next scr refresh
        PressToContinue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block1_MatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block1_Match"-------
for thisComponent in Block1_MatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('First_Match.started', First_Match.tStartRefresh)
thisExp.addData('First_Match.stopped', First_Match.tStopRefresh)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('PressToContinue.started', PressToContinue.tStartRefresh)
thisExp.addData('PressToContinue.stopped', PressToContinue.tStopRefresh)
# the Routine "Block1_Match" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block2_totalloop = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block2_totalloop')
thisExp.addLoop(block2_totalloop)  # add the loop to the experiment
thisBlock2_totalloop = block2_totalloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2_totalloop.rgb)
if thisBlock2_totalloop != None:
    for paramName in thisBlock2_totalloop:
        exec('{} = thisBlock2_totalloop[paramName]'.format(paramName))

for thisBlock2_totalloop in block2_totalloop:
    currentLoop = block2_totalloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_totalloop.rgb)
    if thisBlock2_totalloop != None:
        for paramName in thisBlock2_totalloop:
            exec('{} = thisBlock2_totalloop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    block1_photoloop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Feedback/Feedback_Charlie.xlsx'),
        seed=None, name='block1_photoloop')
    thisExp.addLoop(block1_photoloop)  # add the loop to the experiment
    thisBlock1_photoloop = block1_photoloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1_photoloop.rgb)
    if thisBlock1_photoloop != None:
        for paramName in thisBlock1_photoloop:
            exec('{} = thisBlock1_photoloop[paramName]'.format(paramName))
    
    for thisBlock1_photoloop in block1_photoloop:
        currentLoop = block1_photoloop
        # abbreviate parameter names if possible (e.g. rgb = thisBlock1_photoloop.rgb)
        if thisBlock1_photoloop != None:
            for paramName in thisBlock1_photoloop:
                exec('{} = thisBlock1_photoloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Block1_Photo"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block1_PhotoComponents = [Photo_One, Image_One, text_8]
        for thisComponent in Block1_PhotoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block1_PhotoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block1_Photo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block1_PhotoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block1_PhotoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Photo_One* updates
            if Photo_One.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Photo_One.frameNStart = frameN  # exact frame index
                Photo_One.tStart = t  # local t and not account for scr refresh
                Photo_One.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Photo_One, 'tStartRefresh')  # time at next scr refresh
                Photo_One.setAutoDraw(True)
            if Photo_One.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Photo_One.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Photo_One.tStop = t  # not accounting for scr refresh
                    Photo_One.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Photo_One, 'tStopRefresh')  # time at next scr refresh
                    Photo_One.setAutoDraw(False)
            
            # *Image_One* updates
            if Image_One.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Image_One.frameNStart = frameN  # exact frame index
                Image_One.tStart = t  # local t and not account for scr refresh
                Image_One.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Image_One, 'tStartRefresh')  # time at next scr refresh
                Image_One.setAutoDraw(True)
            if Image_One.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Image_One.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Image_One.tStop = t  # not accounting for scr refresh
                    Image_One.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Image_One, 'tStopRefresh')  # time at next scr refresh
                    Image_One.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block1_PhotoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block1_Photo"-------
        for thisComponent in Block1_PhotoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1_photoloop.addData('Photo_One.started', Photo_One.tStartRefresh)
        block1_photoloop.addData('Photo_One.stopped', Photo_One.tStopRefresh)
        block1_photoloop.addData('Image_One.started', Image_One.tStartRefresh)
        block1_photoloop.addData('Image_One.stopped', Image_One.tStopRefresh)
        block1_photoloop.addData('text_8.started', text_8.tStartRefresh)
        block1_photoloop.addData('text_8.stopped', text_8.tStopRefresh)
        
        # ------Prepare to start Routine "Block1_Waitingforfeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block1_WaitingforfeedbackComponents = [text_5]
        for thisComponent in Block1_WaitingforfeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block1_WaitingforfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block1_Waitingforfeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block1_WaitingforfeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block1_WaitingforfeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block1_WaitingforfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block1_Waitingforfeedback"-------
        for thisComponent in Block1_WaitingforfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1_photoloop.addData('text_5.started', text_5.tStartRefresh)
        block1_photoloop.addData('text_5.stopped', text_5.tStopRefresh)
        
        # ------Prepare to start Routine "Block1Feedback"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block1FeedbackComponents = [text_4, image_7]
        for thisComponent in Block1FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block1FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block1Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block1FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block1FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            if text_4.status == STARTED:  # only update if drawing
                text_4.setText(Response, log=False)
            
            # *image_7* updates
            if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_7.frameNStart = frameN  # exact frame index
                image_7.tStart = t  # local t and not account for scr refresh
                image_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                image_7.setAutoDraw(True)
            if image_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_7.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_7.tStop = t  # not accounting for scr refresh
                    image_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
                    image_7.setAutoDraw(False)
            if image_7.status == STARTED:  # only update if drawing
                image_7.setImage(Graphic, log=False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block1FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block1Feedback"-------
        for thisComponent in Block1FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1_photoloop.addData('text_4.started', text_4.tStartRefresh)
        block1_photoloop.addData('text_4.stopped', text_4.tStopRefresh)
        block1_photoloop.addData('image_7.started', image_7.tStartRefresh)
        block1_photoloop.addData('image_7.stopped', image_7.tStopRefresh)
        
        # ------Prepare to start Routine "Block1_Fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        # keep track of which components have finished
        Block1_FixationComponents = [text_7, key_resp_9]
        for thisComponent in Block1_FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block1_FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block1_Fixation"-------
        while continueRoutine:
            # get current time
            t = Block1_FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block1_FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_7* updates
            if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_7.frameNStart = frameN  # exact frame index
                text_7.tStart = t  # local t and not account for scr refresh
                text_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
                text_7.setAutoDraw(True)
            
            # *key_resp_9* updates
            waitOnFlip = False
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[0].name  # just the first key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block1_FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block1_Fixation"-------
        for thisComponent in Block1_FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block1_photoloop.addData('text_7.started', text_7.tStartRefresh)
        block1_photoloop.addData('text_7.stopped', text_7.tStopRefresh)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        block1_photoloop.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            block1_photoloop.addData('key_resp_9.rt', key_resp_9.rt)
        block1_photoloop.addData('key_resp_9.started', key_resp_9.tStartRefresh)
        block1_photoloop.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
        # the Routine "Block1_Fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block1_photoloop'
    
    
    # ------Prepare to start Routine "Block1_Choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Block1_ChoiceComponents = [lottery_game_choice, computer, self_selected, key_resp_4]
    for thisComponent in Block1_ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block1_ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block1_Choice"-------
    while continueRoutine:
        # get current time
        t = Block1_ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block1_ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lottery_game_choice* updates
        if lottery_game_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lottery_game_choice.frameNStart = frameN  # exact frame index
            lottery_game_choice.tStart = t  # local t and not account for scr refresh
            lottery_game_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lottery_game_choice, 'tStartRefresh')  # time at next scr refresh
            lottery_game_choice.setAutoDraw(True)
        
        # *computer* updates
        if computer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            computer.frameNStart = frameN  # exact frame index
            computer.tStart = t  # local t and not account for scr refresh
            computer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(computer, 'tStartRefresh')  # time at next scr refresh
            computer.setAutoDraw(True)
        
        # *self_selected* updates
        if self_selected.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            self_selected.frameNStart = frameN  # exact frame index
            self_selected.tStart = t  # local t and not account for scr refresh
            self_selected.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(self_selected, 'tStartRefresh')  # time at next scr refresh
            self_selected.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['c', 'm'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        import random
        random_entry = random.choice(computer_choice)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1_ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1_Choice"-------
    for thisComponent in Block1_ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_totalloop.addData('lottery_game_choice.started', lottery_game_choice.tStartRefresh)
    block2_totalloop.addData('lottery_game_choice.stopped', lottery_game_choice.tStopRefresh)
    block2_totalloop.addData('computer.started', computer.tStartRefresh)
    block2_totalloop.addData('computer.stopped', computer.tStopRefresh)
    block2_totalloop.addData('self_selected.started', self_selected.tStartRefresh)
    block2_totalloop.addData('self_selected.stopped', self_selected.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    block2_totalloop.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        block2_totalloop.addData('key_resp_4.rt', key_resp_4.rt)
    block2_totalloop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    block2_totalloop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Block1_Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Block1_Lotterycomputerchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    response_msg = (f'The computer has chosen {random_entry}.')
    if key_resp_4.keys == 'm':
        continueRoutine = False
    computerresponse.setText(response_msg)
    # keep track of which components have finished
    Block1_LotterycomputerchoiceComponents = [lotterycard, Block1_facedowncard, computerresponse]
    for thisComponent in Block1_LotterycomputerchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block1_LotterycomputerchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block1_Lotterycomputerchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block1_LotterycomputerchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block1_LotterycomputerchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lotterycard* updates
        if lotterycard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lotterycard.frameNStart = frameN  # exact frame index
            lotterycard.tStart = t  # local t and not account for scr refresh
            lotterycard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lotterycard, 'tStartRefresh')  # time at next scr refresh
            lotterycard.setAutoDraw(True)
        if lotterycard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lotterycard.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                lotterycard.tStop = t  # not accounting for scr refresh
                lotterycard.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lotterycard, 'tStopRefresh')  # time at next scr refresh
                lotterycard.setAutoDraw(False)
        
        # *Block1_facedowncard* updates
        if Block1_facedowncard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Block1_facedowncard.frameNStart = frameN  # exact frame index
            Block1_facedowncard.tStart = t  # local t and not account for scr refresh
            Block1_facedowncard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Block1_facedowncard, 'tStartRefresh')  # time at next scr refresh
            Block1_facedowncard.setAutoDraw(True)
        if Block1_facedowncard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Block1_facedowncard.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Block1_facedowncard.tStop = t  # not accounting for scr refresh
                Block1_facedowncard.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Block1_facedowncard, 'tStopRefresh')  # time at next scr refresh
                Block1_facedowncard.setAutoDraw(False)
        
        
        #if not Friend_TaskLoop.thisN in [29, 59]: # establishes two blocks per 32 trials
        #    continueRoutine = False # if not trial 31 or 63, skip routine completely
        #else:
        #    Friend_TaskLoop.finished = False
        
        # *computerresponse* updates
        if computerresponse.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            computerresponse.frameNStart = frameN  # exact frame index
            computerresponse.tStart = t  # local t and not account for scr refresh
            computerresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(computerresponse, 'tStartRefresh')  # time at next scr refresh
            computerresponse.setAutoDraw(True)
        if computerresponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > computerresponse.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                computerresponse.tStop = t  # not accounting for scr refresh
                computerresponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(computerresponse, 'tStopRefresh')  # time at next scr refresh
                computerresponse.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1_LotterycomputerchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1_Lotterycomputerchoice"-------
    for thisComponent in Block1_LotterycomputerchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_totalloop.addData('lotterycard.started', lotterycard.tStartRefresh)
    block2_totalloop.addData('lotterycard.stopped', lotterycard.tStopRefresh)
    block2_totalloop.addData('Block1_facedowncard.started', Block1_facedowncard.tStartRefresh)
    block2_totalloop.addData('Block1_facedowncard.stopped', Block1_facedowncard.tStopRefresh)
    block2_totalloop.addData('computerresponse.started', computerresponse.tStartRefresh)
    block2_totalloop.addData('computerresponse.stopped', computerresponse.tStopRefresh)
    
    # ------Prepare to start Routine "Block1_Lotteryselfchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    if key_resp_4.keys == 'c':
        continueRoutine = False
    
    
    responsefeedback.setText(feedback_msg)
    # keep track of which components have finished
    Block1_LotteryselfchoiceComponents = [pickacard, high, low, key_resp_5, responsefeedback, block1_cardimage]
    for thisComponent in Block1_LotteryselfchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block1_LotteryselfchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block1_Lotteryselfchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block1_LotteryselfchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block1_LotteryselfchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pickacard* updates
        if pickacard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pickacard.frameNStart = frameN  # exact frame index
            pickacard.tStart = t  # local t and not account for scr refresh
            pickacard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pickacard, 'tStartRefresh')  # time at next scr refresh
            pickacard.setAutoDraw(True)
        if pickacard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pickacard.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                pickacard.tStop = t  # not accounting for scr refresh
                pickacard.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pickacard, 'tStopRefresh')  # time at next scr refresh
                pickacard.setAutoDraw(False)
        
        # *high* updates
        if high.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            high.frameNStart = frameN  # exact frame index
            high.tStart = t  # local t and not account for scr refresh
            high.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(high, 'tStartRefresh')  # time at next scr refresh
            high.setAutoDraw(True)
        if high.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > high.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                high.tStop = t  # not accounting for scr refresh
                high.frameNStop = frameN  # exact frame index
                win.timeOnFlip(high, 'tStopRefresh')  # time at next scr refresh
                high.setAutoDraw(False)
        
        # *low* updates
        if low.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            low.frameNStart = frameN  # exact frame index
            low.tStart = t  # local t and not account for scr refresh
            low.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(low, 'tStartRefresh')  # time at next scr refresh
            low.setAutoDraw(True)
        if low.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > low.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                low.tStop = t  # not accounting for scr refresh
                low.frameNStop = frameN  # exact frame index
                win.timeOnFlip(low, 'tStopRefresh')  # time at next scr refresh
                low.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['h', 'l'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[0].name  # just the first key pressed
                key_resp_5.rt = _key_resp_5_allKeys[0].rt
        if key_resp_5.keys == 'l':
            feedback_msg = (f'You have chosen lower.')
        elif key_resp_5.keys == 'h':
            feedback_msg = (f'You have chosen higher.')
        else:
            feedback_msg = (f'No response recorded.')
        responsefeedback.setText(feedback_msg)
        print(key_resp_5.keys)
        print(feedback_msg)
        
        #import random
        #random_entry = random.choice(computer_choice)
        #if  key_resp_4.keys == 'c': 
        #    response_msg = (f'The computer has chosen {random_entry}.')
        #elif key_response_4.keys == 'm':
        #    setautodraw(False)    
        #    if key_resp_5 == 'h':
        #        response_msg = (f'You chose higher.')
        #    elif key_resp_5 == 'l':
        #        response_msg = (f'You chose lower.') 
        #else: 
        #    response_msg = (f'Choice not recorded.')
                
        
        
        # *responsefeedback* updates
        if responsefeedback.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            responsefeedback.frameNStart = frameN  # exact frame index
            responsefeedback.tStart = t  # local t and not account for scr refresh
            responsefeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responsefeedback, 'tStartRefresh')  # time at next scr refresh
            responsefeedback.setAutoDraw(True)
        if responsefeedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > responsefeedback.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                responsefeedback.tStop = t  # not accounting for scr refresh
                responsefeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(responsefeedback, 'tStopRefresh')  # time at next scr refresh
                responsefeedback.setAutoDraw(False)
        
        # *block1_cardimage* updates
        if block1_cardimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1_cardimage.frameNStart = frameN  # exact frame index
            block1_cardimage.tStart = t  # local t and not account for scr refresh
            block1_cardimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1_cardimage, 'tStartRefresh')  # time at next scr refresh
            block1_cardimage.setAutoDraw(True)
        if block1_cardimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1_cardimage.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block1_cardimage.tStop = t  # not accounting for scr refresh
                block1_cardimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block1_cardimage, 'tStopRefresh')  # time at next scr refresh
                block1_cardimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1_LotteryselfchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1_Lotteryselfchoice"-------
    for thisComponent in Block1_LotteryselfchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_totalloop.addData('pickacard.started', pickacard.tStartRefresh)
    block2_totalloop.addData('pickacard.stopped', pickacard.tStopRefresh)
    block2_totalloop.addData('high.started', high.tStartRefresh)
    block2_totalloop.addData('high.stopped', high.tStopRefresh)
    block2_totalloop.addData('low.started', low.tStartRefresh)
    block2_totalloop.addData('low.stopped', low.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    block2_totalloop.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        block2_totalloop.addData('key_resp_5.rt', key_resp_5.rt)
    block2_totalloop.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    block2_totalloop.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    block2_totalloop.addData('responsefeedback.started', responsefeedback.tStartRefresh)
    block2_totalloop.addData('responsefeedback.stopped', responsefeedback.tStopRefresh)
    block2_totalloop.addData('block1_cardimage.started', block1_cardimage.tStartRefresh)
    block2_totalloop.addData('block1_cardimage.stopped', block1_cardimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'block2_totalloop'


# ------Prepare to start Routine "Block2_WaitingMatch2"-------
continueRoutine = True
routineTimer.add(9.250000)
# update component parameters for each repeat
# keep track of which components have finished
Block2_WaitingMatch2Components = [secondparnter, syncing2, polygon_2, loading_25, loading_1, loading_50, loading_2, loading_75, loading_3, loading_100, loading_full]
for thisComponent in Block2_WaitingMatch2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block2_WaitingMatch2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block2_WaitingMatch2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block2_WaitingMatch2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block2_WaitingMatch2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *secondparnter* updates
    if secondparnter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        secondparnter.frameNStart = frameN  # exact frame index
        secondparnter.tStart = t  # local t and not account for scr refresh
        secondparnter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(secondparnter, 'tStartRefresh')  # time at next scr refresh
        secondparnter.setAutoDraw(True)
    if secondparnter.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > secondparnter.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            secondparnter.tStop = t  # not accounting for scr refresh
            secondparnter.frameNStop = frameN  # exact frame index
            win.timeOnFlip(secondparnter, 'tStopRefresh')  # time at next scr refresh
            secondparnter.setAutoDraw(False)
    
    # *syncing2* updates
    if syncing2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        syncing2.frameNStart = frameN  # exact frame index
        syncing2.tStart = t  # local t and not account for scr refresh
        syncing2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(syncing2, 'tStartRefresh')  # time at next scr refresh
        syncing2.setAutoDraw(True)
    if syncing2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > syncing2.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            syncing2.tStop = t  # not accounting for scr refresh
            syncing2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(syncing2, 'tStopRefresh')  # time at next scr refresh
            syncing2.setAutoDraw(False)
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    if polygon_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_2.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            polygon_2.tStop = t  # not accounting for scr refresh
            polygon_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(False)
    
    # *loading_25* updates
    if loading_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        loading_25.frameNStart = frameN  # exact frame index
        loading_25.tStart = t  # local t and not account for scr refresh
        loading_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_25, 'tStartRefresh')  # time at next scr refresh
        loading_25.setAutoDraw(True)
    if loading_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_25.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_25.tStop = t  # not accounting for scr refresh
            loading_25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_25, 'tStopRefresh')  # time at next scr refresh
            loading_25.setAutoDraw(False)
    
    # *loading_1* updates
    if loading_1.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        loading_1.frameNStart = frameN  # exact frame index
        loading_1.tStart = t  # local t and not account for scr refresh
        loading_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_1, 'tStartRefresh')  # time at next scr refresh
        loading_1.setAutoDraw(True)
    if loading_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_1.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_1.tStop = t  # not accounting for scr refresh
            loading_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_1, 'tStopRefresh')  # time at next scr refresh
            loading_1.setAutoDraw(False)
    
    # *loading_50* updates
    if loading_50.status == NOT_STARTED and tThisFlip >= 5.50-frameTolerance:
        # keep track of start time/frame for later
        loading_50.frameNStart = frameN  # exact frame index
        loading_50.tStart = t  # local t and not account for scr refresh
        loading_50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_50, 'tStartRefresh')  # time at next scr refresh
        loading_50.setAutoDraw(True)
    if loading_50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_50.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_50.tStop = t  # not accounting for scr refresh
            loading_50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_50, 'tStopRefresh')  # time at next scr refresh
            loading_50.setAutoDraw(False)
    
    # *loading_2* updates
    if loading_2.status == NOT_STARTED and tThisFlip >= 5.50-frameTolerance:
        # keep track of start time/frame for later
        loading_2.frameNStart = frameN  # exact frame index
        loading_2.tStart = t  # local t and not account for scr refresh
        loading_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_2, 'tStartRefresh')  # time at next scr refresh
        loading_2.setAutoDraw(True)
    if loading_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_2.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_2.tStop = t  # not accounting for scr refresh
            loading_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_2, 'tStopRefresh')  # time at next scr refresh
            loading_2.setAutoDraw(False)
    
    # *loading_75* updates
    if loading_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        loading_75.frameNStart = frameN  # exact frame index
        loading_75.tStart = t  # local t and not account for scr refresh
        loading_75.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_75, 'tStartRefresh')  # time at next scr refresh
        loading_75.setAutoDraw(True)
    if loading_75.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_75.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_75.tStop = t  # not accounting for scr refresh
            loading_75.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_75, 'tStopRefresh')  # time at next scr refresh
            loading_75.setAutoDraw(False)
    
    # *loading_3* updates
    if loading_3.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        loading_3.frameNStart = frameN  # exact frame index
        loading_3.tStart = t  # local t and not account for scr refresh
        loading_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_3, 'tStartRefresh')  # time at next scr refresh
        loading_3.setAutoDraw(True)
    if loading_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_3.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_3.tStop = t  # not accounting for scr refresh
            loading_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_3, 'tStopRefresh')  # time at next scr refresh
            loading_3.setAutoDraw(False)
    
    # *loading_100* updates
    if loading_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        loading_100.frameNStart = frameN  # exact frame index
        loading_100.tStart = t  # local t and not account for scr refresh
        loading_100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_100, 'tStartRefresh')  # time at next scr refresh
        loading_100.setAutoDraw(True)
    if loading_100.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_100.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_100.tStop = t  # not accounting for scr refresh
            loading_100.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_100, 'tStopRefresh')  # time at next scr refresh
            loading_100.setAutoDraw(False)
    
    # *loading_full* updates
    if loading_full.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        loading_full.frameNStart = frameN  # exact frame index
        loading_full.tStart = t  # local t and not account for scr refresh
        loading_full.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading_full, 'tStartRefresh')  # time at next scr refresh
        loading_full.setAutoDraw(True)
    if loading_full.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading_full.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading_full.tStop = t  # not accounting for scr refresh
            loading_full.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading_full, 'tStopRefresh')  # time at next scr refresh
            loading_full.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block2_WaitingMatch2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block2_WaitingMatch2"-------
for thisComponent in Block2_WaitingMatch2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('secondparnter.started', secondparnter.tStartRefresh)
thisExp.addData('secondparnter.stopped', secondparnter.tStopRefresh)
thisExp.addData('syncing2.started', syncing2.tStartRefresh)
thisExp.addData('syncing2.stopped', syncing2.tStopRefresh)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('loading_25.started', loading_25.tStartRefresh)
thisExp.addData('loading_25.stopped', loading_25.tStopRefresh)
thisExp.addData('loading_1.started', loading_1.tStartRefresh)
thisExp.addData('loading_1.stopped', loading_1.tStopRefresh)
thisExp.addData('loading_50.started', loading_50.tStartRefresh)
thisExp.addData('loading_50.stopped', loading_50.tStopRefresh)
thisExp.addData('loading_2.started', loading_2.tStartRefresh)
thisExp.addData('loading_2.stopped', loading_2.tStopRefresh)
thisExp.addData('loading_75.started', loading_75.tStartRefresh)
thisExp.addData('loading_75.stopped', loading_75.tStopRefresh)
thisExp.addData('loading_3.started', loading_3.tStartRefresh)
thisExp.addData('loading_3.stopped', loading_3.tStopRefresh)
thisExp.addData('loading_100.started', loading_100.tStartRefresh)
thisExp.addData('loading_100.stopped', loading_100.tStopRefresh)
thisExp.addData('loading_full.started', loading_full.tStartRefresh)
thisExp.addData('loading_full.stopped', loading_full.tStopRefresh)

# ------Prepare to start Routine "Block2_Match"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
Block2_MatchComponents = [nerdface, key_resp_6, Sam]
for thisComponent in Block2_MatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block2_MatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block2_Match"-------
while continueRoutine:
    # get current time
    t = Block2_MatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block2_MatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *nerdface* updates
    if nerdface.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        nerdface.frameNStart = frameN  # exact frame index
        nerdface.tStart = t  # local t and not account for scr refresh
        nerdface.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(nerdface, 'tStartRefresh')  # time at next scr refresh
        nerdface.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[0].name  # just the first key pressed
            key_resp_6.rt = _key_resp_6_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Sam* updates
    if Sam.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Sam.frameNStart = frameN  # exact frame index
        Sam.tStart = t  # local t and not account for scr refresh
        Sam.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Sam, 'tStartRefresh')  # time at next scr refresh
        Sam.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block2_MatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block2_Match"-------
for thisComponent in Block2_MatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('nerdface.started', nerdface.tStartRefresh)
thisExp.addData('nerdface.stopped', nerdface.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Sam.started', Sam.tStartRefresh)
thisExp.addData('Sam.stopped', Sam.tStopRefresh)
# the Routine "Block2_Match" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block2_entireloop = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block2_entireloop')
thisExp.addLoop(block2_entireloop)  # add the loop to the experiment
thisBlock2_entireloop = block2_entireloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2_entireloop.rgb)
if thisBlock2_entireloop != None:
    for paramName in thisBlock2_entireloop:
        exec('{} = thisBlock2_entireloop[paramName]'.format(paramName))

for thisBlock2_entireloop in block2_entireloop:
    currentLoop = block2_entireloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_entireloop.rgb)
    if thisBlock2_entireloop != None:
        for paramName in thisBlock2_entireloop:
            exec('{} = thisBlock2_entireloop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    block2_photoloop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Feedback/Feedback_Sam.xlsx'),
        seed=None, name='block2_photoloop')
    thisExp.addLoop(block2_photoloop)  # add the loop to the experiment
    thisBlock2_photoloop = block2_photoloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_photoloop.rgb)
    if thisBlock2_photoloop != None:
        for paramName in thisBlock2_photoloop:
            exec('{} = thisBlock2_photoloop[paramName]'.format(paramName))
    
    for thisBlock2_photoloop in block2_photoloop:
        currentLoop = block2_photoloop
        # abbreviate parameter names if possible (e.g. rgb = thisBlock2_photoloop.rgb)
        if thisBlock2_photoloop != None:
            for paramName in thisBlock2_photoloop:
                exec('{} = thisBlock2_photoloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Block2_Photo"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block2_PhotoComponents = [image_3, text]
        for thisComponent in Block2_PhotoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block2_PhotoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block2_Photo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block2_PhotoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block2_PhotoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block2_PhotoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block2_Photo"-------
        for thisComponent in Block2_PhotoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2_photoloop.addData('image_3.started', image_3.tStartRefresh)
        block2_photoloop.addData('image_3.stopped', image_3.tStopRefresh)
        block2_photoloop.addData('text.started', text.tStartRefresh)
        block2_photoloop.addData('text.stopped', text.tStopRefresh)
        
        # ------Prepare to start Routine "Block2_Waitingforfeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block2_WaitingforfeedbackComponents = [text_6]
        for thisComponent in Block2_WaitingforfeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block2_WaitingforfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block2_Waitingforfeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block2_WaitingforfeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block2_WaitingforfeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block2_WaitingforfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block2_Waitingforfeedback"-------
        for thisComponent in Block2_WaitingforfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2_photoloop.addData('text_6.started', text_6.tStartRefresh)
        block2_photoloop.addData('text_6.stopped', text_6.tStopRefresh)
        
        # ------Prepare to start Routine "Block2_Feedback"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block2_FeedbackComponents = [text_14, image_11]
        for thisComponent in Block2_FeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block2_FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block2_Feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block2_FeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block2_FeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_14* updates
            if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_14.frameNStart = frameN  # exact frame index
                text_14.tStart = t  # local t and not account for scr refresh
                text_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
                text_14.setAutoDraw(True)
            if text_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_14.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    text_14.tStop = t  # not accounting for scr refresh
                    text_14.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                    text_14.setAutoDraw(False)
            
            # *image_11* updates
            if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_11.frameNStart = frameN  # exact frame index
                image_11.tStart = t  # local t and not account for scr refresh
                image_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                image_11.setAutoDraw(True)
            if image_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_11.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image_11.tStop = t  # not accounting for scr refresh
                    image_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_11, 'tStopRefresh')  # time at next scr refresh
                    image_11.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block2_FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block2_Feedback"-------
        for thisComponent in Block2_FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2_photoloop.addData('text_14.started', text_14.tStartRefresh)
        block2_photoloop.addData('text_14.stopped', text_14.tStopRefresh)
        block2_photoloop.addData('image_11.started', image_11.tStartRefresh)
        block2_photoloop.addData('image_11.stopped', image_11.tStopRefresh)
        
        # ------Prepare to start Routine "Block2_Fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # keep track of which components have finished
        Block2_FixationComponents = [text_13, key_resp_12]
        for thisComponent in Block2_FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block2_FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block2_Fixation"-------
        while continueRoutine:
            # get current time
            t = Block2_FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block2_FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_13* updates
            if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_13.frameNStart = frameN  # exact frame index
                text_13.tStart = t  # local t and not account for scr refresh
                text_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
                text_13.setAutoDraw(True)
            
            # *key_resp_12* updates
            waitOnFlip = False
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[0].name  # just the first key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block2_FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block2_Fixation"-------
        for thisComponent in Block2_FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block2_photoloop.addData('text_13.started', text_13.tStartRefresh)
        block2_photoloop.addData('text_13.stopped', text_13.tStopRefresh)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        block2_photoloop.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            block2_photoloop.addData('key_resp_12.rt', key_resp_12.rt)
        block2_photoloop.addData('key_resp_12.started', key_resp_12.tStartRefresh)
        block2_photoloop.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
        # the Routine "Block2_Fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block2_photoloop'
    
    
    # ------Prepare to start Routine "Block2_choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    Block2_choiceComponents = [choice, block2computer, self, key_resp_7]
    for thisComponent in Block2_choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block2_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block2_choice"-------
    while continueRoutine:
        # get current time
        t = Block2_choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block2_choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choice* updates
        if choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice.frameNStart = frameN  # exact frame index
            choice.tStart = t  # local t and not account for scr refresh
            choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
            choice.setAutoDraw(True)
        
        # *block2computer* updates
        if block2computer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2computer.frameNStart = frameN  # exact frame index
            block2computer.tStart = t  # local t and not account for scr refresh
            block2computer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2computer, 'tStartRefresh')  # time at next scr refresh
            block2computer.setAutoDraw(True)
        
        # *self* updates
        if self.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            self.frameNStart = frameN  # exact frame index
            self.tStart = t  # local t and not account for scr refresh
            self.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(self, 'tStartRefresh')  # time at next scr refresh
            self.setAutoDraw(True)
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['c', 'm'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        import random
        random_entry = random.choice(block2computer_choice)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2_choice"-------
    for thisComponent in Block2_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_entireloop.addData('choice.started', choice.tStartRefresh)
    block2_entireloop.addData('choice.stopped', choice.tStopRefresh)
    block2_entireloop.addData('block2computer.started', block2computer.tStartRefresh)
    block2_entireloop.addData('block2computer.stopped', block2computer.tStopRefresh)
    block2_entireloop.addData('self.started', self.tStartRefresh)
    block2_entireloop.addData('self.stopped', self.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    block2_entireloop.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        block2_entireloop.addData('key_resp_7.rt', key_resp_7.rt)
    block2_entireloop.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    block2_entireloop.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "Block2_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Block2_Lotterycomputerchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    response_msg = (f'The computer has chosen {random_entry}.')
    if key_resp_7.keys == 'm':
        continueRoutine = False
    # keep track of which components have finished
    Block2_LotterycomputerchoiceComponents = [instruction, computerresponse2, card]
    for thisComponent in Block2_LotterycomputerchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block2_LotterycomputerchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block2_Lotterycomputerchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block2_LotterycomputerchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block2_LotterycomputerchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction* updates
        if instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction.frameNStart = frameN  # exact frame index
            instruction.tStart = t  # local t and not account for scr refresh
            instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
            instruction.setAutoDraw(True)
        if instruction.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instruction.tStop = t  # not accounting for scr refresh
                instruction.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instruction, 'tStopRefresh')  # time at next scr refresh
                instruction.setAutoDraw(False)
        
        # *computerresponse2* updates
        if computerresponse2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            computerresponse2.frameNStart = frameN  # exact frame index
            computerresponse2.tStart = t  # local t and not account for scr refresh
            computerresponse2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(computerresponse2, 'tStartRefresh')  # time at next scr refresh
            computerresponse2.setAutoDraw(True)
        if computerresponse2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > computerresponse2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                computerresponse2.tStop = t  # not accounting for scr refresh
                computerresponse2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(computerresponse2, 'tStopRefresh')  # time at next scr refresh
                computerresponse2.setAutoDraw(False)
        
        # *card* updates
        if card.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            card.frameNStart = frameN  # exact frame index
            card.tStart = t  # local t and not account for scr refresh
            card.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(card, 'tStartRefresh')  # time at next scr refresh
            card.setAutoDraw(True)
        if card.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > card.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                card.tStop = t  # not accounting for scr refresh
                card.frameNStop = frameN  # exact frame index
                win.timeOnFlip(card, 'tStopRefresh')  # time at next scr refresh
                card.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2_LotterycomputerchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2_Lotterycomputerchoice"-------
    for thisComponent in Block2_LotterycomputerchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_entireloop.addData('instruction.started', instruction.tStartRefresh)
    block2_entireloop.addData('instruction.stopped', instruction.tStopRefresh)
    block2_entireloop.addData('computerresponse2.started', computerresponse2.tStartRefresh)
    block2_entireloop.addData('computerresponse2.stopped', computerresponse2.tStopRefresh)
    block2_entireloop.addData('card.started', card.tStartRefresh)
    block2_entireloop.addData('card.stopped', card.tStopRefresh)
    
    # ------Prepare to start Routine "Block2_Lotteryselfchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    block2_responsefeedback.setText(block2feedback_msg)
    if key_resp_7.keys == 'c':
        continueRoutine = False
    
    # keep track of which components have finished
    Block2_LotteryselfchoiceComponents = [instructionsforselfchoice2, block2_higherchoice, block2_lowerchoice, key_resp_8, block2_responsefeedback, block2_cardimage]
    for thisComponent in Block2_LotteryselfchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block2_LotteryselfchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block2_Lotteryselfchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block2_LotteryselfchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block2_LotteryselfchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructionsforselfchoice2* updates
        if instructionsforselfchoice2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructionsforselfchoice2.frameNStart = frameN  # exact frame index
            instructionsforselfchoice2.tStart = t  # local t and not account for scr refresh
            instructionsforselfchoice2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructionsforselfchoice2, 'tStartRefresh')  # time at next scr refresh
            instructionsforselfchoice2.setAutoDraw(True)
        if instructionsforselfchoice2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructionsforselfchoice2.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instructionsforselfchoice2.tStop = t  # not accounting for scr refresh
                instructionsforselfchoice2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructionsforselfchoice2, 'tStopRefresh')  # time at next scr refresh
                instructionsforselfchoice2.setAutoDraw(False)
        
        # *block2_higherchoice* updates
        if block2_higherchoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_higherchoice.frameNStart = frameN  # exact frame index
            block2_higherchoice.tStart = t  # local t and not account for scr refresh
            block2_higherchoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_higherchoice, 'tStartRefresh')  # time at next scr refresh
            block2_higherchoice.setAutoDraw(True)
        if block2_higherchoice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_higherchoice.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block2_higherchoice.tStop = t  # not accounting for scr refresh
                block2_higherchoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_higherchoice, 'tStopRefresh')  # time at next scr refresh
                block2_higherchoice.setAutoDraw(False)
        
        # *block2_lowerchoice* updates
        if block2_lowerchoice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_lowerchoice.frameNStart = frameN  # exact frame index
            block2_lowerchoice.tStart = t  # local t and not account for scr refresh
            block2_lowerchoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_lowerchoice, 'tStartRefresh')  # time at next scr refresh
            block2_lowerchoice.setAutoDraw(True)
        if block2_lowerchoice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_lowerchoice.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block2_lowerchoice.tStop = t  # not accounting for scr refresh
                block2_lowerchoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_lowerchoice, 'tStopRefresh')  # time at next scr refresh
                block2_lowerchoice.setAutoDraw(False)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_8.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_8.tStop = t  # not accounting for scr refresh
                key_resp_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_8, 'tStopRefresh')  # time at next scr refresh
                key_resp_8.status = FINISHED
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['h', 'l'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[0].name  # just the first key pressed
                key_resp_8.rt = _key_resp_8_allKeys[0].rt
        
        # *block2_responsefeedback* updates
        if block2_responsefeedback.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            block2_responsefeedback.frameNStart = frameN  # exact frame index
            block2_responsefeedback.tStart = t  # local t and not account for scr refresh
            block2_responsefeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_responsefeedback, 'tStartRefresh')  # time at next scr refresh
            block2_responsefeedback.setAutoDraw(True)
        if block2_responsefeedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_responsefeedback.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block2_responsefeedback.tStop = t  # not accounting for scr refresh
                block2_responsefeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_responsefeedback, 'tStopRefresh')  # time at next scr refresh
                block2_responsefeedback.setAutoDraw(False)
        if key_resp_8.keys == 'l':
            block2feedback_msg = (f'You have chosen lower.')
        elif key_resp_8.keys == 'h':
            block2feedback_msg = (f'You have chosen higher.')
        else:
            block2feedback_msg = (f'No response recorded.')
        block2responsefeedback.setText(feedback_msg)
        print(key_resp_5.keys)
        print(feedback_msg)
        
        
        # *block2_cardimage* updates
        if block2_cardimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_cardimage.frameNStart = frameN  # exact frame index
            block2_cardimage.tStart = t  # local t and not account for scr refresh
            block2_cardimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_cardimage, 'tStartRefresh')  # time at next scr refresh
            block2_cardimage.setAutoDraw(True)
        if block2_cardimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_cardimage.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block2_cardimage.tStop = t  # not accounting for scr refresh
                block2_cardimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_cardimage, 'tStopRefresh')  # time at next scr refresh
                block2_cardimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2_LotteryselfchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2_Lotteryselfchoice"-------
    for thisComponent in Block2_LotteryselfchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_entireloop.addData('instructionsforselfchoice2.started', instructionsforselfchoice2.tStartRefresh)
    block2_entireloop.addData('instructionsforselfchoice2.stopped', instructionsforselfchoice2.tStopRefresh)
    block2_entireloop.addData('block2_higherchoice.started', block2_higherchoice.tStartRefresh)
    block2_entireloop.addData('block2_higherchoice.stopped', block2_higherchoice.tStopRefresh)
    block2_entireloop.addData('block2_lowerchoice.started', block2_lowerchoice.tStartRefresh)
    block2_entireloop.addData('block2_lowerchoice.stopped', block2_lowerchoice.tStopRefresh)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    block2_entireloop.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        block2_entireloop.addData('key_resp_8.rt', key_resp_8.rt)
    block2_entireloop.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    block2_entireloop.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    block2_entireloop.addData('block2_responsefeedback.started', block2_responsefeedback.tStartRefresh)
    block2_entireloop.addData('block2_responsefeedback.stopped', block2_responsefeedback.tStopRefresh)
    block2_entireloop.addData('block2_cardimage.started', block2_cardimage.tStartRefresh)
    block2_entireloop.addData('block2_cardimage.stopped', block2_cardimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'block2_entireloop'


# ------Prepare to start Routine "Block3_waitingtomatch"-------
continueRoutine = True
routineTimer.add(9.250000)
# update component parameters for each repeat
# keep track of which components have finished
Block3_waitingtomatchComponents = [block3_match, syncing3, polygon3, loading25, block3loading1, loading50, block3loading2, loading75, blockloading3, loading100, block3loadingfull]
for thisComponent in Block3_waitingtomatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block3_waitingtomatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block3_waitingtomatch"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Block3_waitingtomatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block3_waitingtomatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block3_match* updates
    if block3_match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block3_match.frameNStart = frameN  # exact frame index
        block3_match.tStart = t  # local t and not account for scr refresh
        block3_match.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3_match, 'tStartRefresh')  # time at next scr refresh
        block3_match.setAutoDraw(True)
    if block3_match.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > block3_match.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            block3_match.tStop = t  # not accounting for scr refresh
            block3_match.frameNStop = frameN  # exact frame index
            win.timeOnFlip(block3_match, 'tStopRefresh')  # time at next scr refresh
            block3_match.setAutoDraw(False)
    
    # *syncing3* updates
    if syncing3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        syncing3.frameNStart = frameN  # exact frame index
        syncing3.tStart = t  # local t and not account for scr refresh
        syncing3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(syncing3, 'tStartRefresh')  # time at next scr refresh
        syncing3.setAutoDraw(True)
    if syncing3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > syncing3.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            syncing3.tStop = t  # not accounting for scr refresh
            syncing3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(syncing3, 'tStopRefresh')  # time at next scr refresh
            syncing3.setAutoDraw(False)
    
    # *polygon3* updates
    if polygon3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        polygon3.frameNStart = frameN  # exact frame index
        polygon3.tStart = t  # local t and not account for scr refresh
        polygon3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon3, 'tStartRefresh')  # time at next scr refresh
        polygon3.setAutoDraw(True)
    if polygon3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon3.tStartRefresh + 6.25-frameTolerance:
            # keep track of stop time/frame for later
            polygon3.tStop = t  # not accounting for scr refresh
            polygon3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon3, 'tStopRefresh')  # time at next scr refresh
            polygon3.setAutoDraw(False)
    
    # *loading25* updates
    if loading25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        loading25.frameNStart = frameN  # exact frame index
        loading25.tStart = t  # local t and not account for scr refresh
        loading25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading25, 'tStartRefresh')  # time at next scr refresh
        loading25.setAutoDraw(True)
    if loading25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading25.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading25.tStop = t  # not accounting for scr refresh
            loading25.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading25, 'tStopRefresh')  # time at next scr refresh
            loading25.setAutoDraw(False)
    
    # *block3loading1* updates
    if block3loading1.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
        # keep track of start time/frame for later
        block3loading1.frameNStart = frameN  # exact frame index
        block3loading1.tStart = t  # local t and not account for scr refresh
        block3loading1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3loading1, 'tStartRefresh')  # time at next scr refresh
        block3loading1.setAutoDraw(True)
    if block3loading1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > block3loading1.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            block3loading1.tStop = t  # not accounting for scr refresh
            block3loading1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(block3loading1, 'tStopRefresh')  # time at next scr refresh
            block3loading1.setAutoDraw(False)
    
    # *loading50* updates
    if loading50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        loading50.frameNStart = frameN  # exact frame index
        loading50.tStart = t  # local t and not account for scr refresh
        loading50.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading50, 'tStartRefresh')  # time at next scr refresh
        loading50.setAutoDraw(True)
    if loading50.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading50.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading50.tStop = t  # not accounting for scr refresh
            loading50.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading50, 'tStopRefresh')  # time at next scr refresh
            loading50.setAutoDraw(False)
    
    # *block3loading2* updates
    if block3loading2.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
        # keep track of start time/frame for later
        block3loading2.frameNStart = frameN  # exact frame index
        block3loading2.tStart = t  # local t and not account for scr refresh
        block3loading2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3loading2, 'tStartRefresh')  # time at next scr refresh
        block3loading2.setAutoDraw(True)
    if block3loading2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > block3loading2.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            block3loading2.tStop = t  # not accounting for scr refresh
            block3loading2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(block3loading2, 'tStopRefresh')  # time at next scr refresh
            block3loading2.setAutoDraw(False)
    
    # *loading75* updates
    if loading75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        loading75.frameNStart = frameN  # exact frame index
        loading75.tStart = t  # local t and not account for scr refresh
        loading75.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading75, 'tStartRefresh')  # time at next scr refresh
        loading75.setAutoDraw(True)
    if loading75.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading75.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading75.tStop = t  # not accounting for scr refresh
            loading75.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading75, 'tStopRefresh')  # time at next scr refresh
            loading75.setAutoDraw(False)
    
    # *blockloading3* updates
    if blockloading3.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
        # keep track of start time/frame for later
        blockloading3.frameNStart = frameN  # exact frame index
        blockloading3.tStart = t  # local t and not account for scr refresh
        blockloading3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(blockloading3, 'tStartRefresh')  # time at next scr refresh
        blockloading3.setAutoDraw(True)
    if blockloading3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > blockloading3.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            blockloading3.tStop = t  # not accounting for scr refresh
            blockloading3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blockloading3, 'tStopRefresh')  # time at next scr refresh
            blockloading3.setAutoDraw(False)
    
    # *loading100* updates
    if loading100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        loading100.frameNStart = frameN  # exact frame index
        loading100.tStart = t  # local t and not account for scr refresh
        loading100.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(loading100, 'tStartRefresh')  # time at next scr refresh
        loading100.setAutoDraw(True)
    if loading100.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > loading100.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            loading100.tStop = t  # not accounting for scr refresh
            loading100.frameNStop = frameN  # exact frame index
            win.timeOnFlip(loading100, 'tStopRefresh')  # time at next scr refresh
            loading100.setAutoDraw(False)
    
    # *block3loadingfull* updates
    if block3loadingfull.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
        # keep track of start time/frame for later
        block3loadingfull.frameNStart = frameN  # exact frame index
        block3loadingfull.tStart = t  # local t and not account for scr refresh
        block3loadingfull.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3loadingfull, 'tStartRefresh')  # time at next scr refresh
        block3loadingfull.setAutoDraw(True)
    if block3loadingfull.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > block3loadingfull.tStartRefresh + 1.25-frameTolerance:
            # keep track of stop time/frame for later
            block3loadingfull.tStop = t  # not accounting for scr refresh
            block3loadingfull.frameNStop = frameN  # exact frame index
            win.timeOnFlip(block3loadingfull, 'tStopRefresh')  # time at next scr refresh
            block3loadingfull.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block3_waitingtomatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block3_waitingtomatch"-------
for thisComponent in Block3_waitingtomatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('block3_match.started', block3_match.tStartRefresh)
thisExp.addData('block3_match.stopped', block3_match.tStopRefresh)
thisExp.addData('syncing3.started', syncing3.tStartRefresh)
thisExp.addData('syncing3.stopped', syncing3.tStopRefresh)
thisExp.addData('polygon3.started', polygon3.tStartRefresh)
thisExp.addData('polygon3.stopped', polygon3.tStopRefresh)
thisExp.addData('loading25.started', loading25.tStartRefresh)
thisExp.addData('loading25.stopped', loading25.tStopRefresh)
thisExp.addData('block3loading1.started', block3loading1.tStartRefresh)
thisExp.addData('block3loading1.stopped', block3loading1.tStopRefresh)
thisExp.addData('loading50.started', loading50.tStartRefresh)
thisExp.addData('loading50.stopped', loading50.tStopRefresh)
thisExp.addData('block3loading2.started', block3loading2.tStartRefresh)
thisExp.addData('block3loading2.stopped', block3loading2.tStopRefresh)
thisExp.addData('loading75.started', loading75.tStartRefresh)
thisExp.addData('loading75.stopped', loading75.tStopRefresh)
thisExp.addData('blockloading3.started', blockloading3.tStartRefresh)
thisExp.addData('blockloading3.stopped', blockloading3.tStopRefresh)
thisExp.addData('loading100.started', loading100.tStartRefresh)
thisExp.addData('loading100.stopped', loading100.tStopRefresh)
thisExp.addData('block3loadingfull.started', block3loadingfull.tStartRefresh)
thisExp.addData('block3loadingfull.stopped', block3loadingfull.tStopRefresh)

# ------Prepare to start Routine "Block3_Match"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
Block3_MatchComponents = [block3match, key_resp_10, image_8]
for thisComponent in Block3_MatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Block3_MatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Block3_Match"-------
while continueRoutine:
    # get current time
    t = Block3_MatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Block3_MatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block3match* updates
    if block3match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block3match.frameNStart = frameN  # exact frame index
        block3match.tStart = t  # local t and not account for scr refresh
        block3match.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block3match, 'tStartRefresh')  # time at next scr refresh
        block3match.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[0].name  # just the first key pressed
            key_resp_10.rt = _key_resp_10_allKeys[0].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Block3_MatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Block3_Match"-------
for thisComponent in Block3_MatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('block3match.started', block3match.tStartRefresh)
thisExp.addData('block3match.stopped', block3match.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
# the Routine "Block3_Match" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block3_entireloop = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block3_entireloop')
thisExp.addLoop(block3_entireloop)  # add the loop to the experiment
thisBlock3_entireloop = block3_entireloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3_entireloop.rgb)
if thisBlock3_entireloop != None:
    for paramName in thisBlock3_entireloop:
        exec('{} = thisBlock3_entireloop[paramName]'.format(paramName))

for thisBlock3_entireloop in block3_entireloop:
    currentLoop = block3_entireloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3_entireloop.rgb)
    if thisBlock3_entireloop != None:
        for paramName in thisBlock3_entireloop:
            exec('{} = thisBlock3_entireloop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    block3_photoloop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Feedback/Feedback_Riley.xlsx'),
        seed=None, name='block3_photoloop')
    thisExp.addLoop(block3_photoloop)  # add the loop to the experiment
    thisBlock3_photoloop = block3_photoloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3_photoloop.rgb)
    if thisBlock3_photoloop != None:
        for paramName in thisBlock3_photoloop:
            exec('{} = thisBlock3_photoloop[paramName]'.format(paramName))
    
    for thisBlock3_photoloop in block3_photoloop:
        currentLoop = block3_photoloop
        # abbreviate parameter names if possible (e.g. rgb = thisBlock3_photoloop.rgb)
        if thisBlock3_photoloop != None:
            for paramName in thisBlock3_photoloop:
                exec('{} = thisBlock3_photoloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Block3_Photo"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block3_PhotoComponents = [image_9, text_9]
        for thisComponent in Block3_PhotoComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block3_PhotoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block3_Photo"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block3_PhotoClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block3_PhotoClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_9* updates
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                image_9.setAutoDraw(True)
            if image_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_9.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    image_9.tStop = t  # not accounting for scr refresh
                    image_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
                    image_9.setAutoDraw(False)
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                    text_9.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block3_PhotoComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block3_Photo"-------
        for thisComponent in Block3_PhotoComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block3_photoloop.addData('image_9.started', image_9.tStartRefresh)
        block3_photoloop.addData('image_9.stopped', image_9.tStopRefresh)
        block3_photoloop.addData('text_9.started', text_9.tStartRefresh)
        block3_photoloop.addData('text_9.stopped', text_9.tStopRefresh)
        
        # ------Prepare to start Routine "Block3_Waitingforfeedback"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block3_WaitingforfeedbackComponents = [text_10]
        for thisComponent in Block3_WaitingforfeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block3_WaitingforfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block3_Waitingforfeedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block3_WaitingforfeedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block3_WaitingforfeedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                    text_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block3_WaitingforfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block3_Waitingforfeedback"-------
        for thisComponent in Block3_WaitingforfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block3_photoloop.addData('text_10.started', text_10.tStartRefresh)
        block3_photoloop.addData('text_10.stopped', text_10.tStopRefresh)
        
        # ------Prepare to start Routine "Block3_feedback"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        Block3_feedbackComponents = [text_11, image_10]
        for thisComponent in Block3_feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block3_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block3_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Block3_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block3_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                text_11.setAutoDraw(True)
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                    text_11.setAutoDraw(False)
            
            # *image_10* updates
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                image_10.setAutoDraw(True)
            if image_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_10.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_10.tStop = t  # not accounting for scr refresh
                    image_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_10, 'tStopRefresh')  # time at next scr refresh
                    image_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block3_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block3_feedback"-------
        for thisComponent in Block3_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block3_photoloop.addData('text_11.started', text_11.tStartRefresh)
        block3_photoloop.addData('text_11.stopped', text_11.tStopRefresh)
        block3_photoloop.addData('image_10.started', image_10.tStartRefresh)
        block3_photoloop.addData('image_10.stopped', image_10.tStopRefresh)
        
        # ------Prepare to start Routine "Block3_Fixation"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        Block3_FixationComponents = [text_12, key_resp_11]
        for thisComponent in Block3_FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Block3_FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Block3_Fixation"-------
        while continueRoutine:
            # get current time
            t = Block3_FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Block3_FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_12* updates
            if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_12.frameNStart = frameN  # exact frame index
                text_12.tStart = t  # local t and not account for scr refresh
                text_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
                text_12.setAutoDraw(True)
            
            # *key_resp_11* updates
            waitOnFlip = False
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[0].name  # just the first key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Block3_FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Block3_Fixation"-------
        for thisComponent in Block3_FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        block3_photoloop.addData('text_12.started', text_12.tStartRefresh)
        block3_photoloop.addData('text_12.stopped', text_12.tStopRefresh)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        block3_photoloop.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            block3_photoloop.addData('key_resp_11.rt', key_resp_11.rt)
        block3_photoloop.addData('key_resp_11.started', key_resp_11.tStartRefresh)
        block3_photoloop.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
        # the Routine "Block3_Fixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'block3_photoloop'
    
    
    # ------Prepare to start Routine "Block3_Choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_13.keys = []
    key_resp_13.rt = []
    _key_resp_13_allKeys = []
    # keep track of which components have finished
    Block3_ChoiceComponents = [key_resp_13, block3_choice, block3_computer, block3_self]
    for thisComponent in Block3_ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block3_ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block3_Choice"-------
    while continueRoutine:
        # get current time
        t = Block3_ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block3_ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        import random
        random_entry = random.choice(block3computer_choice)
        
        # *key_resp_13* updates
        waitOnFlip = False
        if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_13.frameNStart = frameN  # exact frame index
            key_resp_13.tStart = t  # local t and not account for scr refresh
            key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
            key_resp_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_13.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_13.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _key_resp_13_allKeys.extend(theseKeys)
            if len(_key_resp_13_allKeys):
                key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *block3_choice* updates
        if block3_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_choice.frameNStart = frameN  # exact frame index
            block3_choice.tStart = t  # local t and not account for scr refresh
            block3_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_choice, 'tStartRefresh')  # time at next scr refresh
            block3_choice.setAutoDraw(True)
        if block3_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_choice.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                block3_choice.tStop = t  # not accounting for scr refresh
                block3_choice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_choice, 'tStopRefresh')  # time at next scr refresh
                block3_choice.setAutoDraw(False)
        
        # *block3_computer* updates
        if block3_computer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_computer.frameNStart = frameN  # exact frame index
            block3_computer.tStart = t  # local t and not account for scr refresh
            block3_computer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_computer, 'tStartRefresh')  # time at next scr refresh
            block3_computer.setAutoDraw(True)
        if block3_computer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_computer.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                block3_computer.tStop = t  # not accounting for scr refresh
                block3_computer.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_computer, 'tStopRefresh')  # time at next scr refresh
                block3_computer.setAutoDraw(False)
        
        # *block3_self* updates
        if block3_self.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_self.frameNStart = frameN  # exact frame index
            block3_self.tStart = t  # local t and not account for scr refresh
            block3_self.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_self, 'tStartRefresh')  # time at next scr refresh
            block3_self.setAutoDraw(True)
        if block3_self.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_self.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                block3_self.tStop = t  # not accounting for scr refresh
                block3_self.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_self, 'tStopRefresh')  # time at next scr refresh
                block3_self.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block3_ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block3_Choice"-------
    for thisComponent in Block3_ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_13.keys in ['', [], None]:  # No response was made
        key_resp_13.keys = None
    block3_entireloop.addData('key_resp_13.keys',key_resp_13.keys)
    if key_resp_13.keys != None:  # we had a response
        block3_entireloop.addData('key_resp_13.rt', key_resp_13.rt)
    block3_entireloop.addData('key_resp_13.started', key_resp_13.tStartRefresh)
    block3_entireloop.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
    block3_entireloop.addData('block3_choice.started', block3_choice.tStartRefresh)
    block3_entireloop.addData('block3_choice.stopped', block3_choice.tStopRefresh)
    block3_entireloop.addData('block3_computer.started', block3_computer.tStartRefresh)
    block3_entireloop.addData('block3_computer.stopped', block3_computer.tStopRefresh)
    block3_entireloop.addData('block3_self.started', block3_self.tStartRefresh)
    block3_entireloop.addData('block3_self.stopped', block3_self.tStopRefresh)
    # the Routine "Block3_Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Block3_lotterycomputerchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    response_msg = (f'The computer has chosen {random_entry}.')
    if key_resp_13.keys == 'm':
        continueRoutine = False
    # keep track of which components have finished
    Block3_lotterycomputerchoiceComponents = [Block3_lotcomputerchoice, Block3_computerresponse, block3_cardimage]
    for thisComponent in Block3_lotterycomputerchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block3_lotterycomputerchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block3_lotterycomputerchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block3_lotterycomputerchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block3_lotterycomputerchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block3_lotcomputerchoice* updates
        if Block3_lotcomputerchoice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Block3_lotcomputerchoice.frameNStart = frameN  # exact frame index
            Block3_lotcomputerchoice.tStart = t  # local t and not account for scr refresh
            Block3_lotcomputerchoice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Block3_lotcomputerchoice, 'tStartRefresh')  # time at next scr refresh
            Block3_lotcomputerchoice.setAutoDraw(True)
        if Block3_lotcomputerchoice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Block3_lotcomputerchoice.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                Block3_lotcomputerchoice.tStop = t  # not accounting for scr refresh
                Block3_lotcomputerchoice.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Block3_lotcomputerchoice, 'tStopRefresh')  # time at next scr refresh
                Block3_lotcomputerchoice.setAutoDraw(False)
        
        # *Block3_computerresponse* updates
        if Block3_computerresponse.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            Block3_computerresponse.frameNStart = frameN  # exact frame index
            Block3_computerresponse.tStart = t  # local t and not account for scr refresh
            Block3_computerresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Block3_computerresponse, 'tStartRefresh')  # time at next scr refresh
            Block3_computerresponse.setAutoDraw(True)
        if Block3_computerresponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Block3_computerresponse.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Block3_computerresponse.tStop = t  # not accounting for scr refresh
                Block3_computerresponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Block3_computerresponse, 'tStopRefresh')  # time at next scr refresh
                Block3_computerresponse.setAutoDraw(False)
        
        # *block3_cardimage* updates
        if block3_cardimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_cardimage.frameNStart = frameN  # exact frame index
            block3_cardimage.tStart = t  # local t and not account for scr refresh
            block3_cardimage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_cardimage, 'tStartRefresh')  # time at next scr refresh
            block3_cardimage.setAutoDraw(True)
        if block3_cardimage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_cardimage.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block3_cardimage.tStop = t  # not accounting for scr refresh
                block3_cardimage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_cardimage, 'tStopRefresh')  # time at next scr refresh
                block3_cardimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block3_lotterycomputerchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block3_lotterycomputerchoice"-------
    for thisComponent in Block3_lotterycomputerchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block3_entireloop.addData('Block3_lotcomputerchoice.started', Block3_lotcomputerchoice.tStartRefresh)
    block3_entireloop.addData('Block3_lotcomputerchoice.stopped', Block3_lotcomputerchoice.tStopRefresh)
    block3_entireloop.addData('Block3_computerresponse.started', Block3_computerresponse.tStartRefresh)
    block3_entireloop.addData('Block3_computerresponse.stopped', Block3_computerresponse.tStopRefresh)
    block3_entireloop.addData('block3_cardimage.started', block3_cardimage.tStartRefresh)
    block3_entireloop.addData('block3_cardimage.stopped', block3_cardimage.tStopRefresh)
    
    # ------Prepare to start Routine "Block3_lotteryselfchoice"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    key_resp_14.keys = []
    key_resp_14.rt = []
    _key_resp_14_allKeys = []
    if key_resp_13.keys == 'c':
        continueRoutine = False
    # keep track of which components have finished
    Block3_lotteryselfchoiceComponents = [block3_lotteryintstructions, block3_higher, block3_lower, key_resp_14, image_12, block3_feedbackresponse]
    for thisComponent in Block3_lotteryselfchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Block3_lotteryselfchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Block3_lotteryselfchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block3_lotteryselfchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Block3_lotteryselfchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block3_lotteryintstructions* updates
        if block3_lotteryintstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_lotteryintstructions.frameNStart = frameN  # exact frame index
            block3_lotteryintstructions.tStart = t  # local t and not account for scr refresh
            block3_lotteryintstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_lotteryintstructions, 'tStartRefresh')  # time at next scr refresh
            block3_lotteryintstructions.setAutoDraw(True)
        if block3_lotteryintstructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_lotteryintstructions.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block3_lotteryintstructions.tStop = t  # not accounting for scr refresh
                block3_lotteryintstructions.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_lotteryintstructions, 'tStopRefresh')  # time at next scr refresh
                block3_lotteryintstructions.setAutoDraw(False)
        
        # *block3_higher* updates
        if block3_higher.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_higher.frameNStart = frameN  # exact frame index
            block3_higher.tStart = t  # local t and not account for scr refresh
            block3_higher.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_higher, 'tStartRefresh')  # time at next scr refresh
            block3_higher.setAutoDraw(True)
        if block3_higher.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_higher.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block3_higher.tStop = t  # not accounting for scr refresh
                block3_higher.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_higher, 'tStopRefresh')  # time at next scr refresh
                block3_higher.setAutoDraw(False)
        
        # *block3_lower* updates
        if block3_lower.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_lower.frameNStart = frameN  # exact frame index
            block3_lower.tStart = t  # local t and not account for scr refresh
            block3_lower.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_lower, 'tStartRefresh')  # time at next scr refresh
            block3_lower.setAutoDraw(True)
        if block3_lower.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_lower.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                block3_lower.tStop = t  # not accounting for scr refresh
                block3_lower.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_lower, 'tStopRefresh')  # time at next scr refresh
                block3_lower.setAutoDraw(False)
        
        # *key_resp_14* updates
        waitOnFlip = False
        if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_14.frameNStart = frameN  # exact frame index
            key_resp_14.tStart = t  # local t and not account for scr refresh
            key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
            key_resp_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_14.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_14.tStop = t  # not accounting for scr refresh
                key_resp_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_14, 'tStopRefresh')  # time at next scr refresh
                key_resp_14.status = FINISHED
        if key_resp_14.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_14.getKeys(keyList=['h', 'l'], waitRelease=False)
            _key_resp_14_allKeys.extend(theseKeys)
            if len(_key_resp_14_allKeys):
                key_resp_14.keys = _key_resp_14_allKeys[0].name  # just the first key pressed
                key_resp_14.rt = _key_resp_14_allKeys[0].rt
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
                image_12.setAutoDraw(False)
        
        # *block3_feedbackresponse* updates
        if block3_feedbackresponse.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            block3_feedbackresponse.frameNStart = frameN  # exact frame index
            block3_feedbackresponse.tStart = t  # local t and not account for scr refresh
            block3_feedbackresponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_feedbackresponse, 'tStartRefresh')  # time at next scr refresh
            block3_feedbackresponse.setAutoDraw(True)
        if block3_feedbackresponse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_feedbackresponse.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                block3_feedbackresponse.tStop = t  # not accounting for scr refresh
                block3_feedbackresponse.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_feedbackresponse, 'tStopRefresh')  # time at next scr refresh
                block3_feedbackresponse.setAutoDraw(False)
        if key_resp_14.keys == 'l':
            block3feedback_msg = (f'You have chosen lower.')
        elif key_resp_14.keys == 'h':
            block3feedback_msg = (f'You have chosen higher.')
        else:
            block3feedback_msg = (f'No response recorded.')
        block3responsefeedback.setText(feedback_msg)
        print(key_resp_5.keys)
        print(feedback_msg)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block3_lotteryselfchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block3_lotteryselfchoice"-------
    for thisComponent in Block3_lotteryselfchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block3_entireloop.addData('block3_lotteryintstructions.started', block3_lotteryintstructions.tStartRefresh)
    block3_entireloop.addData('block3_lotteryintstructions.stopped', block3_lotteryintstructions.tStopRefresh)
    block3_entireloop.addData('block3_higher.started', block3_higher.tStartRefresh)
    block3_entireloop.addData('block3_higher.stopped', block3_higher.tStopRefresh)
    block3_entireloop.addData('block3_lower.started', block3_lower.tStartRefresh)
    block3_entireloop.addData('block3_lower.stopped', block3_lower.tStopRefresh)
    # check responses
    if key_resp_14.keys in ['', [], None]:  # No response was made
        key_resp_14.keys = None
    block3_entireloop.addData('key_resp_14.keys',key_resp_14.keys)
    if key_resp_14.keys != None:  # we had a response
        block3_entireloop.addData('key_resp_14.rt', key_resp_14.rt)
    block3_entireloop.addData('key_resp_14.started', key_resp_14.tStartRefresh)
    block3_entireloop.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
    block3_entireloop.addData('image_12.started', image_12.tStartRefresh)
    block3_entireloop.addData('image_12.stopped', image_12.tStopRefresh)
    block3_entireloop.addData('block3_feedbackresponse.started', block3_feedbackresponse.tStartRefresh)
    block3_entireloop.addData('block3_feedbackresponse.stopped', block3_feedbackresponse.tStopRefresh)
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'block3_entireloop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
