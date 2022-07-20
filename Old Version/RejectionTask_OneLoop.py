#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Wed May 18 16:19:55 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.3')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
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
psychopyVersion = '2022.1.3'
expName = 'RejectionTask_OneLoop'  # from the Builder filename that created this script
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
    originPath='/Users/jordansiegel/Documents/PhD/Research/Second Year Project/Rejection_Task 2/RejectionTask_OneLoop.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

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
    text='To begin, you will be assigned a partner at random by the computer. \n\n\nNext, you will share your instagram photos with your partner. \n\n\nAfter sharing each photo, your partner will give you feedback on whether they liked or disliked your photo.\n\nPress space to continue.',
    font='Open Sans',
    pos=(0, 0.08), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "WaitingToMatch"
WaitingToMatchClock = core.Clock()
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
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.2,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-2.0, interpolate=True)
Loading_25 = visual.Rect(
    win=win, name='Loading_25',
    width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
    ori=0.0, pos=(-0.375, 0), anchor='center',
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
    ori=0.0, pos=(-0.25, 0), anchor='center',
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
    ori=0.0, pos=(-.125, 0), anchor='center',
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
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
text_100 = visual.TextStim(win=win, name='text_100',
    text='100%',
    font='Open Sans',
    pos=(0, -.2), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "Partner_Match"
Partner_MatchClock = core.Clock()
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
    image='Images/sunglass emoji.jpeg', mask=None, anchor='center',
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

# Initialize components for Routine "Photo_Share"
Photo_ShareClock = core.Clock()
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
    image='Images/Participant Images.xlsx', mask=None, anchor='center',
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

# Initialize components for Routine "Waitingforfeedback"
WaitingforfeedbackClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='Waiting…',
    font='Open Sans',
    pos=(0, 0.0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Feedback_2"
Feedback_2Clock = core.Clock()
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
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press space to share your next photo.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
lottery_game_choice = visual.TextStim(win=win, name='lottery_game_choice',
    text='You now have the option to play a lottery game! The game is guessing whether a facedown card is will be higher or lower than a certain number.\n\nYou may have chose to have the computer play on your behalf or you may play yourself. If you would like the computer to play on your behalf press ‘c’. If you would like to play press ‘m’.\n\nIf you chose to play, you will have 3 seconds to record your choice.\n',
    font='Open Sans',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0.0, 
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


# Initialize components for Routine "Lotterycomputerchoice"
LotterycomputerchoiceClock = core.Clock()
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
    image='Images/facedown card.jpeg', mask=None, anchor='center',
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

# Initialize components for Routine "Lotteryselfchoice"
LotteryselfchoiceClock = core.Clock()
pickacard = visual.TextStim(win=win, name='pickacard',
    text='Please select whether you believe the card will be higher or lower than 5. Press ‘h’ for higher or ‘l’ for lower.',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
high = visual.TextStim(win=win, name='high',
    text='Higher',
    font='Open Sans',
    pos=(0.3, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
low = visual.TextStim(win=win, name='low',
    text='Lower',
    font='Open Sans',
    pos=(-.3, -.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_5 = keyboard.Keyboard()
responsefeedback = visual.TextStim(win=win, name='responsefeedback',
    text='',
    font='Open Sans',
    pos=(0, -0.39), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
block1_cardimage = visual.ImageStim(
    win=win,
    name='block1_cardimage', 
    image='Images/facedown card.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# Initialize components for Routine "Continue"
ContinueClock = core.Clock()
block1_continue = visual.TextStim(win=win, name='block1_continue',
    text='Press space to resume sharing your photos.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

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

# set up handler to look after randomisation of conditions etc
entiretaskloop = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='entiretaskloop')
thisExp.addLoop(entiretaskloop)  # add the loop to the experiment
thisEntiretaskloop = entiretaskloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
if thisEntiretaskloop != None:
    for paramName in thisEntiretaskloop:
        exec('{} = thisEntiretaskloop[paramName]'.format(paramName))

for thisEntiretaskloop in entiretaskloop:
    currentLoop = entiretaskloop
    # abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
    if thisEntiretaskloop != None:
        for paramName in thisEntiretaskloop:
            exec('{} = thisEntiretaskloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "WaitingToMatch"-------
    continueRoutine = True
    routineTimer.add(9.250000)
    # update component parameters for each repeat
    # keep track of which components have finished
    WaitingToMatchComponents = [Match, syncing, Transparent, Loading_25, text_25, Loading_50, text_50, Loading_75, text_75, Loading_100, text_100]
    for thisComponent in WaitingToMatchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    WaitingToMatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "WaitingToMatch"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = WaitingToMatchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=WaitingToMatchClock)
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
        for thisComponent in WaitingToMatchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "WaitingToMatch"-------
    for thisComponent in WaitingToMatchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    entiretaskloop.addData('Match.started', Match.tStartRefresh)
    entiretaskloop.addData('Match.stopped', Match.tStopRefresh)
    entiretaskloop.addData('syncing.started', syncing.tStartRefresh)
    entiretaskloop.addData('syncing.stopped', syncing.tStopRefresh)
    entiretaskloop.addData('Transparent.started', Transparent.tStartRefresh)
    entiretaskloop.addData('Transparent.stopped', Transparent.tStopRefresh)
    entiretaskloop.addData('Loading_25.started', Loading_25.tStartRefresh)
    entiretaskloop.addData('Loading_25.stopped', Loading_25.tStopRefresh)
    entiretaskloop.addData('text_25.started', text_25.tStartRefresh)
    entiretaskloop.addData('text_25.stopped', text_25.tStopRefresh)
    entiretaskloop.addData('Loading_50.started', Loading_50.tStartRefresh)
    entiretaskloop.addData('Loading_50.stopped', Loading_50.tStopRefresh)
    entiretaskloop.addData('text_50.started', text_50.tStartRefresh)
    entiretaskloop.addData('text_50.stopped', text_50.tStopRefresh)
    entiretaskloop.addData('Loading_75.started', Loading_75.tStartRefresh)
    entiretaskloop.addData('Loading_75.stopped', Loading_75.tStopRefresh)
    entiretaskloop.addData('text_75.started', text_75.tStartRefresh)
    entiretaskloop.addData('text_75.stopped', text_75.tStopRefresh)
    entiretaskloop.addData('Loading_100.started', Loading_100.tStartRefresh)
    entiretaskloop.addData('Loading_100.stopped', Loading_100.tStopRefresh)
    entiretaskloop.addData('text_100.started', text_100.tStartRefresh)
    entiretaskloop.addData('text_100.stopped', text_100.tStopRefresh)
    
    # ------Prepare to start Routine "Partner_Match"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Partner_MatchComponents = [First_Match, image, key_resp_3, PressToContinue]
    for thisComponent in Partner_MatchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Partner_MatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Partner_Match"-------
    while continueRoutine:
        # get current time
        t = Partner_MatchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Partner_MatchClock)
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
        for thisComponent in Partner_MatchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Partner_Match"-------
    for thisComponent in Partner_MatchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    entiretaskloop.addData('First_Match.started', First_Match.tStartRefresh)
    entiretaskloop.addData('First_Match.stopped', First_Match.tStopRefresh)
    entiretaskloop.addData('image.started', image.tStartRefresh)
    entiretaskloop.addData('image.stopped', image.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    entiretaskloop.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        entiretaskloop.addData('key_resp_3.rt', key_resp_3.rt)
    entiretaskloop.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    entiretaskloop.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    entiretaskloop.addData('PressToContinue.started', PressToContinue.tStartRefresh)
    entiretaskloop.addData('PressToContinue.stopped', PressToContinue.tStopRefresh)
    # the Routine "Partner_Match" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    choiceloop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='choiceloop')
    thisExp.addLoop(choiceloop)  # add the loop to the experiment
    thisChoiceloop = choiceloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisChoiceloop.rgb)
    if thisChoiceloop != None:
        for paramName in thisChoiceloop:
            exec('{} = thisChoiceloop[paramName]'.format(paramName))
    
    for thisChoiceloop in choiceloop:
        currentLoop = choiceloop
        # abbreviate parameter names if possible (e.g. rgb = thisChoiceloop.rgb)
        if thisChoiceloop != None:
            for paramName in thisChoiceloop:
                exec('{} = thisChoiceloop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        photoloop = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Feedback/Feedback_Charlie.xlsx'),
            seed=None, name='photoloop')
        thisExp.addLoop(photoloop)  # add the loop to the experiment
        thisPhotoloop = photoloop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPhotoloop.rgb)
        if thisPhotoloop != None:
            for paramName in thisPhotoloop:
                exec('{} = thisPhotoloop[paramName]'.format(paramName))
        
        for thisPhotoloop in photoloop:
            currentLoop = photoloop
            # abbreviate parameter names if possible (e.g. rgb = thisPhotoloop.rgb)
            if thisPhotoloop != None:
                for paramName in thisPhotoloop:
                    exec('{} = thisPhotoloop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Photo_Share"-------
            continueRoutine = True
            routineTimer.add(3.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Photo_ShareComponents = [Photo_One, Image_One, text_8]
            for thisComponent in Photo_ShareComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Photo_ShareClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Photo_Share"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Photo_ShareClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Photo_ShareClock)
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
                    if tThisFlipGlobal > text_8.tStartRefresh + 3-frameTolerance:
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
                for thisComponent in Photo_ShareComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Photo_Share"-------
            for thisComponent in Photo_ShareComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            photoloop.addData('Photo_One.started', Photo_One.tStartRefresh)
            photoloop.addData('Photo_One.stopped', Photo_One.tStopRefresh)
            photoloop.addData('Image_One.started', Image_One.tStartRefresh)
            photoloop.addData('Image_One.stopped', Image_One.tStopRefresh)
            photoloop.addData('text_8.started', text_8.tStartRefresh)
            photoloop.addData('text_8.stopped', text_8.tStopRefresh)
            
            # ------Prepare to start Routine "Waitingforfeedback"-------
            continueRoutine = True
            routineTimer.add(5.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            WaitingforfeedbackComponents = [text_5]
            for thisComponent in WaitingforfeedbackComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            WaitingforfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Waitingforfeedback"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = WaitingforfeedbackClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=WaitingforfeedbackClock)
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
                for thisComponent in WaitingforfeedbackComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Waitingforfeedback"-------
            for thisComponent in WaitingforfeedbackComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            photoloop.addData('text_5.started', text_5.tStartRefresh)
            photoloop.addData('text_5.stopped', text_5.tStopRefresh)
            
            # ------Prepare to start Routine "Feedback_2"-------
            continueRoutine = True
            routineTimer.add(3.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            Feedback_2Components = [text_4, image_7]
            for thisComponent in Feedback_2Components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            Feedback_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Feedback_2"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = Feedback_2Clock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=Feedback_2Clock)
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
                for thisComponent in Feedback_2Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Feedback_2"-------
            for thisComponent in Feedback_2Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            photoloop.addData('text_4.started', text_4.tStartRefresh)
            photoloop.addData('text_4.stopped', text_4.tStopRefresh)
            photoloop.addData('image_7.started', image_7.tStartRefresh)
            photoloop.addData('image_7.stopped', image_7.tStopRefresh)
            
            # ------Prepare to start Routine "Fixation"-------
            continueRoutine = True
            # update component parameters for each repeat
            key_resp_9.keys = []
            key_resp_9.rt = []
            _key_resp_9_allKeys = []
            # keep track of which components have finished
            FixationComponents = [text_7, key_resp_9]
            for thisComponent in FixationComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Fixation"-------
            while continueRoutine:
                # get current time
                t = FixationClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=FixationClock)
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
                for thisComponent in FixationComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Fixation"-------
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            photoloop.addData('text_7.started', text_7.tStartRefresh)
            photoloop.addData('text_7.stopped', text_7.tStopRefresh)
            # check responses
            if key_resp_9.keys in ['', [], None]:  # No response was made
                key_resp_9.keys = None
            photoloop.addData('key_resp_9.keys',key_resp_9.keys)
            if key_resp_9.keys != None:  # we had a response
                photoloop.addData('key_resp_9.rt', key_resp_9.rt)
            photoloop.addData('key_resp_9.started', key_resp_9.tStartRefresh)
            photoloop.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
            # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'photoloop'
        
        
        # ------Prepare to start Routine "Choice"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        ChoiceComponents = [lottery_game_choice, computer, self_selected, key_resp_4]
        for thisComponent in ChoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Choice"-------
        while continueRoutine:
            # get current time
            t = ChoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
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
                theseKeys = key_resp_4.getKeys(keyList=['c','m'], waitRelease=False)
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
            for thisComponent in ChoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice"-------
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        choiceloop.addData('lottery_game_choice.started', lottery_game_choice.tStartRefresh)
        choiceloop.addData('lottery_game_choice.stopped', lottery_game_choice.tStopRefresh)
        choiceloop.addData('computer.started', computer.tStartRefresh)
        choiceloop.addData('computer.stopped', computer.tStopRefresh)
        choiceloop.addData('self_selected.started', self_selected.tStartRefresh)
        choiceloop.addData('self_selected.stopped', self_selected.tStopRefresh)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        choiceloop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            choiceloop.addData('key_resp_4.rt', key_resp_4.rt)
        choiceloop.addData('key_resp_4.started', key_resp_4.tStartRefresh)
        choiceloop.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
        # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Lotterycomputerchoice"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        response_msg = (f'The computer has chosen {random_entry}.')
        if key_resp_4.keys == 'm':
            continueRoutine = False
        computerresponse.setText(response_msg)
        # keep track of which components have finished
        LotterycomputerchoiceComponents = [lotterycard, Block1_facedowncard, computerresponse]
        for thisComponent in LotterycomputerchoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LotterycomputerchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Lotterycomputerchoice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = LotterycomputerchoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LotterycomputerchoiceClock)
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
            for thisComponent in LotterycomputerchoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Lotterycomputerchoice"-------
        for thisComponent in LotterycomputerchoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        choiceloop.addData('lotterycard.started', lotterycard.tStartRefresh)
        choiceloop.addData('lotterycard.stopped', lotterycard.tStopRefresh)
        choiceloop.addData('Block1_facedowncard.started', Block1_facedowncard.tStartRefresh)
        choiceloop.addData('Block1_facedowncard.stopped', Block1_facedowncard.tStopRefresh)
        choiceloop.addData('computerresponse.started', computerresponse.tStartRefresh)
        choiceloop.addData('computerresponse.stopped', computerresponse.tStopRefresh)
        
        # ------Prepare to start Routine "Lotteryselfchoice"-------
        continueRoutine = True
        routineTimer.add(8.000000)
        # update component parameters for each repeat
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        if key_resp_4.keys == 'c':
            continueRoutine = False
        
        
        responsefeedback.setText(feedback_msg)
        # keep track of which components have finished
        LotteryselfchoiceComponents = [pickacard, high, low, key_resp_5, responsefeedback, block1_cardimage]
        for thisComponent in LotteryselfchoiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LotteryselfchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Lotteryselfchoice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = LotteryselfchoiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LotteryselfchoiceClock)
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
                if tThisFlipGlobal > pickacard.tStartRefresh + 8-frameTolerance:
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
                if tThisFlipGlobal > high.tStartRefresh + 8-frameTolerance:
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
                if tThisFlipGlobal > low.tStartRefresh + 8-frameTolerance:
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
                theseKeys = key_resp_5.getKeys(keyList=['h','l'], waitRelease=False)
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
                if tThisFlipGlobal > responsefeedback.tStartRefresh + 4-frameTolerance:
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
                if tThisFlipGlobal > block1_cardimage.tStartRefresh + 8-frameTolerance:
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
            for thisComponent in LotteryselfchoiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Lotteryselfchoice"-------
        for thisComponent in LotteryselfchoiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        choiceloop.addData('pickacard.started', pickacard.tStartRefresh)
        choiceloop.addData('pickacard.stopped', pickacard.tStopRefresh)
        choiceloop.addData('high.started', high.tStartRefresh)
        choiceloop.addData('high.stopped', high.tStopRefresh)
        choiceloop.addData('low.started', low.tStartRefresh)
        choiceloop.addData('low.stopped', low.tStopRefresh)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        choiceloop.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            choiceloop.addData('key_resp_5.rt', key_resp_5.rt)
        choiceloop.addData('key_resp_5.started', key_resp_5.tStartRefresh)
        choiceloop.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
        choiceloop.addData('responsefeedback.started', responsefeedback.tStartRefresh)
        choiceloop.addData('responsefeedback.stopped', responsefeedback.tStopRefresh)
        choiceloop.addData('block1_cardimage.started', block1_cardimage.tStartRefresh)
        choiceloop.addData('block1_cardimage.stopped', block1_cardimage.tStopRefresh)
        
        # ------Prepare to start Routine "Continue"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp_15.keys = []
        key_resp_15.rt = []
        _key_resp_15_allKeys = []
        # keep track of which components have finished
        ContinueComponents = [block1_continue, key_resp_15]
        for thisComponent in ContinueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ContinueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Continue"-------
        while continueRoutine:
            # get current time
            t = ContinueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ContinueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *block1_continue* updates
            if block1_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                block1_continue.frameNStart = frameN  # exact frame index
                block1_continue.tStart = t  # local t and not account for scr refresh
                block1_continue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(block1_continue, 'tStartRefresh')  # time at next scr refresh
                block1_continue.setAutoDraw(True)
            
            # *key_resp_15* updates
            waitOnFlip = False
            if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_15.frameNStart = frameN  # exact frame index
                key_resp_15.tStart = t  # local t and not account for scr refresh
                key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
                key_resp_15.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_15.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_15_allKeys.extend(theseKeys)
                if len(_key_resp_15_allKeys):
                    key_resp_15.keys = _key_resp_15_allKeys[0].name  # just the first key pressed
                    key_resp_15.rt = _key_resp_15_allKeys[0].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ContinueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Continue"-------
        for thisComponent in ContinueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        choiceloop.addData('block1_continue.started', block1_continue.tStartRefresh)
        choiceloop.addData('block1_continue.stopped', block1_continue.tStopRefresh)
        # check responses
        if key_resp_15.keys in ['', [], None]:  # No response was made
            key_resp_15.keys = None
        choiceloop.addData('key_resp_15.keys',key_resp_15.keys)
        if key_resp_15.keys != None:  # we had a response
            choiceloop.addData('key_resp_15.rt', key_resp_15.rt)
        choiceloop.addData('key_resp_15.started', key_resp_15.tStartRefresh)
        choiceloop.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
        # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'choiceloop'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'entiretaskloop'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
