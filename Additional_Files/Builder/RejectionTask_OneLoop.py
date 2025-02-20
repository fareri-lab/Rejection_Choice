#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.5),
    on Fri Feb  7 14:11:13 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2024.1.5')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from saliencyrating_code
saliencerating = ''
salienceratingtext=''
rating_forsalience = ''    

# Run 'Before Experiment' code from stresslevelslider
stresslevel = ''
stressleveltext = ''
rating_forstress = ''
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.5'
expName = 'RejectionTask_OneLoop'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 900]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s/%s_%s_%s' % (expInfo['participant'],expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/jordansiegel/Documents/GitHub/Rejection_Choice/Additional_Files/Builder/RejectionTask_OneLoop.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1.0000, -1.0000, -1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('endwelcomescreen_keys') is None:
        # initialise endwelcomescreen_keys
        endwelcomescreen_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endwelcomescreen_keys',
        )
    if deviceManager.getDevice('endinstructionscreen_keys') is None:
        # initialise endinstructionscreen_keys
        endinstructionscreen_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endinstructionscreen_keys',
        )
    if deviceManager.getDevice('endpartnermatch_keys') is None:
        # initialise endpartnermatch_keys
        endpartnermatch_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='endpartnermatch_keys',
        )
    if deviceManager.getDevice('sharenextphoto_key') is None:
        # initialise sharenextphoto_key
        sharenextphoto_key = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='sharenextphoto_key',
        )
    if deviceManager.getDevice('choice_keys') is None:
        # initialise choice_keys
        choice_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='choice_keys',
        )
    if deviceManager.getDevice('lotteryguess_keys') is None:
        # initialise lotteryguess_keys
        lotteryguess_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='lotteryguess_keys',
        )
    if deviceManager.getDevice('resumeafterlottery_keys') is None:
        # initialise resumeafterlottery_keys
        resumeafterlottery_keys = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resumeafterlottery_keys',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('stresslevel_keypress') is None:
        # initialise stresslevel_keypress
        stresslevel_keypress = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='stresslevel_keypress',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Welcome_Screen" ---
    Welcome = visual.TextStim(win=win, name='Welcome',
        text='Welcome to the Instagram Sharing Task!\n\n\nToday you will have the opportunity to share some of your Instagram photos with other participants and receive feedback.\n\n\n\nPress space to continue.\n',
        font='Open Sans',
        pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endwelcomescreen_keys = keyboard.Keyboard(deviceName='endwelcomescreen_keys')
    # Run 'Begin Experiment' code from buildspreadsheet
    partnermatch = ''
    partneravatar = ''
    
    
    # --- Initialize components for Routine "test" ---
    
    # --- Initialize components for Routine "First_Instructions" ---
    FirstInstructions = visual.TextStim(win=win, name='FirstInstructions',
        text='To begin, you will be assigned a partner at random by the computer. Next, your instagram photos will be shared with your partner. After each photo is shared, your partner will give you feedback on whether they liked or disliked your photo. You will have the chance to share your photos with 3 different partners during todays task.\n\n\nYou may be eligible throughout the task to participate in a lottery, which you may play yourself or have the computer play on your behalf. Further instructions about this task will be provided should you be eligible to participate.\n\n\nPress space to continue.',
        font='Open Sans',
        pos=(0,0), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    endinstructionscreen_keys = keyboard.Keyboard(deviceName='endinstructionscreen_keys')
    
    # --- Initialize components for Routine "partner_code" ---
    # Run 'Begin Experiment' code from partnermatchcode
    partnermatch = ''
    partneravatar = ''
    
    
    # --- Initialize components for Routine "WaitingToMatch" ---
    Match_text = visual.TextStim(win=win, name='Match_text',
        text='You will now be matched with a game partner selected at random by the computer.',
        font='Open Sans',
        pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    syncing_text = visual.TextStim(win=win, name='syncing_text',
        text='Syncing…',
        font='Open Sans',
        pos=(0, 0.3), height=0.12, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_0 = visual.TextStim(win=win, name='text_0',
        text='0%',
        font='Open Sans',
        pos=(0, -0.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    Transparent = visual.Rect(
        win=win, name='Transparent',
        width=(1, 0.1)[0], height=(1, 0.1)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.2,     colorSpace='rgb',  lineColor='white', fillColor=[0.0000, 0.0000, 0.0000],
        opacity=None, depth=-4.0, interpolate=True)
    Loading_25 = visual.Rect(
        win=win, name='Loading_25',
        width=(0.25, 0.1)[0], height=(0.25, 0.1)[1],
        ori=0.0, pos=(-0.375, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-5.0, interpolate=True)
    text_25 = visual.TextStim(win=win, name='text_25',
        text='25%',
        font='Open Sans',
        pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    Loading_50 = visual.Rect(
        win=win, name='Loading_50',
        width=(.5, 0.1)[0], height=(.5, 0.1)[1],
        ori=0.0, pos=(-0.25, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-7.0, interpolate=True)
    text_50 = visual.TextStim(win=win, name='text_50',
        text='50%',
        font='Open Sans',
        pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    Loading_75 = visual.Rect(
        win=win, name='Loading_75',
        width=(0.75, 0.1)[0], height=(0.75, 0.1)[1],
        ori=0.0, pos=(-.125, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-9.0, interpolate=True)
    text_75 = visual.TextStim(win=win, name='text_75',
        text='75%',
        font='Open Sans',
        pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-10.0);
    Loading_100 = visual.Rect(
        win=win, name='Loading_100',
        width=(1, 0.1)[0], height=(1, 0.1)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-11.0, interpolate=True)
    text_100 = visual.TextStim(win=win, name='text_100',
        text='100%',
        font='Open Sans',
        pos=(0, -.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "Partner_Match" ---
    Youhavematched = visual.TextStim(win=win, name='Youhavematched',
        text='',
        font='Open Sans',
        pos=(0, 0.6), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    partneremoji_image = visual.ImageStim(
        win=win,
        name='partneremoji_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    endpartnermatch_keys = keyboard.Keyboard(deviceName='endpartnermatch_keys')
    PressToContinue = visual.TextStim(win=win, name='PressToContinue',
        text='Press space to continue.',
        font='Open Sans',
        pos=(0, -0.6), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "Photo_Share" ---
    photobeingshared_text = visual.TextStim(win=win, name='photobeingshared_text',
        text='This photo is now being shared',
        font='Open Sans',
        pos=(0.0,0.6), height=0.09, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    waitforfeedback_text = visual.TextStim(win=win, name='waitforfeedback_text',
        text='Please wait for feedback.',
        font='Open Sans',
        pos=(0, -0.6), height=0.09, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from initiatefeedbackresponses
    feedbackresponses = ''
    fdbkimage = ''
    participantimage_image = visual.ImageStim(
        win=win,
        name='participantimage_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Waitingforfeedback" ---
    waiting_text = visual.TextStim(win=win, name='waiting_text',
        text='Waiting…',
        font='Open Sans',
        pos=(0, 0.0), height=0.15, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "feedback" ---
    displayfeedback_text = visual.TextStim(win=win, name='displayfeedback_text',
        text='',
        font='Open Sans',
        pos=(0, 0.75), height=0.12, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    fdbkimage_image = visual.ImageStim(
        win=win,
        name='fdbkimage_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.75, 1.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    # Run 'Begin Experiment' code from initiatelottery_code
    startlottery = ''
    
    # --- Initialize components for Routine "continuesharing" ---
    presstosharenextphoto_text = visual.TextStim(win=win, name='presstosharenextphoto_text',
        text='Press space to share your next photo.',
        font='Open Sans',
        pos=(0, 0), height=0.09, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    sharenextphoto_key = keyboard.Keyboard(deviceName='sharenextphoto_key')
    
    # --- Initialize components for Routine "Choice" ---
    lotterychoice_text = visual.TextStim(win=win, name='lotterychoice_text',
        text='You now have the option to play a lottery game! To play, a guess whether the upside down card is higher or lower than 5 needs to be made.\n\nYou can either have the computer guess on your behalf or you may make a guess yourself. If you would like the computer to make the guess on your behalf press ‘c’. If you would like to guess yourself press ‘s’. \n\n\nYou will have 3 seconds to decide.\n',
        font='Open Sans',
        pos=(0, 0.3), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    computer_text = visual.TextStim(win=win, name='computer_text',
        text='Computer',
        font='Open Sans',
        pos=(-.3, -.4), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    self_text = visual.TextStim(win=win, name='self_text',
        text='Self',
        font='Open Sans',
        pos=(0.3, -.4), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    # Run 'Begin Experiment' code from setvariables_code
    response_msg = ' '
    feedback_msg = ' '
    computer_choice = ['lower','lower','lower','lower','lower','higher','higher','higher','higher','higher']
    selfrunOrNot = ''
    comprunOrNot = ''
    resumetext= ''
    choice_keys = keyboard.Keyboard(deviceName='choice_keys')
    
    # --- Initialize components for Routine "Lotterycomputerchoice" ---
    lotterycard = visual.TextStim(win=win, name='lotterycard',
        text='The computer will select whether it believes the card will be higher or lower than 5.',
        font='Open Sans',
        pos=(0, 0.6), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Block1_facedowncard = visual.ImageStim(
        win=win,
        name='Block1_facedowncard', 
        image='Images/facedown card.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.75, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    computerresponse = visual.TextStim(win=win, name='computerresponse',
        text='',
        font='Open Sans',
        pos=(0, -0.4), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "Lotteryselfchoice" ---
    pickacard_text = visual.TextStim(win=win, name='pickacard_text',
        text='Please select whether you believe the card will be higher or lower than 5. Press ‘h’ for higher or ‘l’ for lower.',
        font='Open Sans',
        pos=(0, 0.65), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    higher_text = visual.TextStim(win=win, name='higher_text',
        text='Higher',
        font='Open Sans',
        pos=(0.3, -0.5), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    lower_text = visual.TextStim(win=win, name='lower_text',
        text='Lower',
        font='Open Sans',
        pos=(-.3, -.5), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    lotteryguess_keys = keyboard.Keyboard(deviceName='lotteryguess_keys')
    responsefeedback = visual.TextStim(win=win, name='responsefeedback',
        text='',
        font='Open Sans',
        pos=(0, -0.59), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    block1_cardimage = visual.ImageStim(
        win=win,
        name='block1_cardimage', 
        image='Images/facedown card.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.75, 0.75),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    
    # --- Initialize components for Routine "Continue" ---
    resumeafterlottery_keys = keyboard.Keyboard(deviceName='resumeafterlottery_keys')
    resumetext_text = visual.TextStim(win=win, name='resumetext_text',
        text='',
        font='Open Sans',
        pos=(0, 0), height=0.12, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "SalienceRating" ---
    # Run 'Begin Experiment' code from saliencyrating_code
    salience_slider = visual.Slider(win=win, name='slider',
        startValue=999, size=(1.0, 0.1), pos=(0, -0.4), units=None,
        labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5), granularity=0.0,
        style='rating', styleTweaks=('labels45', 'triangleMarker'), opacity=None,
        labelColor='white', markerColor='cornflowerblue', lineColor='white', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05, 
        flip=False, ori=0.0, depth=-5, readOnly=False)
    saliencequestion_text = visual.TextStim(win=win, name='saliencequestion_text',
        text='',
        font='Open Sans',
        pos=(0, 0.6), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    salienceavatar_image = visual.ImageStim(
        win=win,
        name='salienceavatar_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.3, 0.55),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    saliencecontinue_text = visual.TextStim(win=win, name='saliencecontinue_text',
        text='Press space to enter rating and continue.',
        font='Open Sans',
        pos=(0, -0.8), height=0.07, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    displayrating_text = visual.TextStim(win=win, name='displayrating_text',
        text='',
        font='Open Sans',
        pos=(0, -0.65), height=0.065, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "StressLevel" ---
    # Run 'Begin Experiment' code from stresslevelslider
    stress_slider = visual.Slider(win=win, name='slider',
        startValue=999, size=(1.0, 0.1), pos=(0, -0.4), units=None,
        labels=(1, 2, 3, 4, 5, 6, 7, 8, 9), ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9), granularity=0.0,
        style='rating', styleTweaks=('labels45', 'triangleMarker'), opacity=None,
        labelColor='white', markerColor='cornflowerblue', lineColor='white', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-5, readOnly=False)
    stresslevel_text = visual.TextStim(win=win, name='stresslevel_text',
        text='',
        font='Open Sans',
        pos=(0, 0.3), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    stresslevel_keypress = keyboard.Keyboard(deviceName='stresslevel_keypress')
    displaystressrating_text = visual.TextStim(win=win, name='displaystressrating_text',
        text='',
        font='Open Sans',
        pos=(0, -0.65), height=0.08, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Welcome_Screen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Welcome_Screen.started', globalClock.getTime(format='float'))
    # create starting attributes for endwelcomescreen_keys
    endwelcomescreen_keys.keys = []
    endwelcomescreen_keys.rt = []
    _endwelcomescreen_keys_allKeys = []
    # keep track of which components have finished
    Welcome_ScreenComponents = [Welcome, endwelcomescreen_keys]
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
    frameN = -1
    
    # --- Run Routine "Welcome_Screen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Welcome* updates
        
        # if Welcome is starting this frame...
        if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Welcome.frameNStart = frameN  # exact frame index
            Welcome.tStart = t  # local t and not account for scr refresh
            Welcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Welcome.started')
            # update status
            Welcome.status = STARTED
            Welcome.setAutoDraw(True)
        
        # if Welcome is active this frame...
        if Welcome.status == STARTED:
            # update params
            pass
        
        # *endwelcomescreen_keys* updates
        waitOnFlip = False
        
        # if endwelcomescreen_keys is starting this frame...
        if endwelcomescreen_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endwelcomescreen_keys.frameNStart = frameN  # exact frame index
            endwelcomescreen_keys.tStart = t  # local t and not account for scr refresh
            endwelcomescreen_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endwelcomescreen_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endwelcomescreen_keys.started')
            # update status
            endwelcomescreen_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endwelcomescreen_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endwelcomescreen_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endwelcomescreen_keys.status == STARTED and not waitOnFlip:
            theseKeys = endwelcomescreen_keys.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _endwelcomescreen_keys_allKeys.extend(theseKeys)
            if len(_endwelcomescreen_keys_allKeys):
                endwelcomescreen_keys.keys = _endwelcomescreen_keys_allKeys[-1].name  # just the last key pressed
                endwelcomescreen_keys.rt = _endwelcomescreen_keys_allKeys[-1].rt
                endwelcomescreen_keys.duration = _endwelcomescreen_keys_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Welcome_ScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Welcome_Screen" ---
    for thisComponent in Welcome_ScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Welcome_Screen.stopped', globalClock.getTime(format='float'))
    # check responses
    if endwelcomescreen_keys.keys in ['', [], None]:  # No response was made
        endwelcomescreen_keys.keys = None
    thisExp.addData('endwelcomescreen_keys.keys',endwelcomescreen_keys.keys)
    if endwelcomescreen_keys.keys != None:  # we had a response
        thisExp.addData('endwelcomescreen_keys.rt', endwelcomescreen_keys.rt)
        thisExp.addData('endwelcomescreen_keys.duration', endwelcomescreen_keys.duration)
    thisExp.nextEntry()
    # the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "test" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('test.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    testComponents = []
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test" ---
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('test.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "First_Instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('First_Instructions.started', globalClock.getTime(format='float'))
    # create starting attributes for endinstructionscreen_keys
    endinstructionscreen_keys.keys = []
    endinstructionscreen_keys.rt = []
    _endinstructionscreen_keys_allKeys = []
    # keep track of which components have finished
    First_InstructionsComponents = [FirstInstructions, endinstructionscreen_keys]
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
    frameN = -1
    
    # --- Run Routine "First_Instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FirstInstructions* updates
        
        # if FirstInstructions is starting this frame...
        if FirstInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FirstInstructions.frameNStart = frameN  # exact frame index
            FirstInstructions.tStart = t  # local t and not account for scr refresh
            FirstInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FirstInstructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FirstInstructions.started')
            # update status
            FirstInstructions.status = STARTED
            FirstInstructions.setAutoDraw(True)
        
        # if FirstInstructions is active this frame...
        if FirstInstructions.status == STARTED:
            # update params
            pass
        
        # *endinstructionscreen_keys* updates
        waitOnFlip = False
        
        # if endinstructionscreen_keys is starting this frame...
        if endinstructionscreen_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endinstructionscreen_keys.frameNStart = frameN  # exact frame index
            endinstructionscreen_keys.tStart = t  # local t and not account for scr refresh
            endinstructionscreen_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endinstructionscreen_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'endinstructionscreen_keys.started')
            # update status
            endinstructionscreen_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(endinstructionscreen_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(endinstructionscreen_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if endinstructionscreen_keys.status == STARTED and not waitOnFlip:
            theseKeys = endinstructionscreen_keys.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _endinstructionscreen_keys_allKeys.extend(theseKeys)
            if len(_endinstructionscreen_keys_allKeys):
                endinstructionscreen_keys.keys = _endinstructionscreen_keys_allKeys[-1].name  # just the last key pressed
                endinstructionscreen_keys.rt = _endinstructionscreen_keys_allKeys[-1].rt
                endinstructionscreen_keys.duration = _endinstructionscreen_keys_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in First_InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "First_Instructions" ---
    for thisComponent in First_InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('First_Instructions.stopped', globalClock.getTime(format='float'))
    # check responses
    if endinstructionscreen_keys.keys in ['', [], None]:  # No response was made
        endinstructionscreen_keys.keys = None
    thisExp.addData('endinstructionscreen_keys.keys',endinstructionscreen_keys.keys)
    if endinstructionscreen_keys.keys != None:  # we had a response
        thisExp.addData('endinstructionscreen_keys.rt', endinstructionscreen_keys.rt)
        thisExp.addData('endinstructionscreen_keys.duration', endinstructionscreen_keys.duration)
    thisExp.nextEntry()
    # the Routine "First_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    entiretaskloop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Dummy_Spreadsheet.csv'),
        seed=None, name='entiretaskloop')
    thisExp.addLoop(entiretaskloop)  # add the loop to the experiment
    thisEntiretaskloop = entiretaskloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
    if thisEntiretaskloop != None:
        for paramName in thisEntiretaskloop:
            globals()[paramName] = thisEntiretaskloop[paramName]
    
    for thisEntiretaskloop in entiretaskloop:
        currentLoop = entiretaskloop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisEntiretaskloop.rgb)
        if thisEntiretaskloop != None:
            for paramName in thisEntiretaskloop:
                globals()[paramName] = thisEntiretaskloop[paramName]
        
        # --- Prepare to start Routine "partner_code" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('partner_code.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        partner_codeComponents = []
        for thisComponent in partner_codeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "partner_code" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in partner_codeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "partner_code" ---
        for thisComponent in partner_codeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('partner_code.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from partnermatchcode
        partnermatch = (f'You have matched with: {Partner}')
        if Partner == 'Sam':
            partneravatar='Images/nerdemoji_nobackground.png'
        if Partner == 'Riley':
            partneravatar='Images/sunglassemoji_nobackground.png'
        elif Partner == 'Charlie':
            partneravatar='Images/smilingemoji.tiff'
        # the Routine "partner_code" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "WaitingToMatch" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('WaitingToMatch.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from showloadingbar
        if TrialNumber not in [1, 31, 61]: # establishes two blocks per 32 trials
            continueRoutine = False # if not trial 31 or 63, skip routine completely
        # keep track of which components have finished
        WaitingToMatchComponents = [Match_text, syncing_text, text_0, Transparent, Loading_25, text_25, Loading_50, text_50, Loading_75, text_75, Loading_100, text_100]
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
        frameN = -1
        
        # --- Run Routine "WaitingToMatch" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 9.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Match_text* updates
            
            # if Match_text is starting this frame...
            if Match_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Match_text.frameNStart = frameN  # exact frame index
                Match_text.tStart = t  # local t and not account for scr refresh
                Match_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Match_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Match_text.started')
                # update status
                Match_text.status = STARTED
                Match_text.setAutoDraw(True)
            
            # if Match_text is active this frame...
            if Match_text.status == STARTED:
                # update params
                pass
            
            # if Match_text is stopping this frame...
            if Match_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Match_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    Match_text.tStop = t  # not accounting for scr refresh
                    Match_text.tStopRefresh = tThisFlipGlobal  # on global time
                    Match_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Match_text.stopped')
                    # update status
                    Match_text.status = FINISHED
                    Match_text.setAutoDraw(False)
            
            # *syncing_text* updates
            
            # if syncing_text is starting this frame...
            if syncing_text.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                syncing_text.frameNStart = frameN  # exact frame index
                syncing_text.tStart = t  # local t and not account for scr refresh
                syncing_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(syncing_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'syncing_text.started')
                # update status
                syncing_text.status = STARTED
                syncing_text.setAutoDraw(True)
            
            # if syncing_text is active this frame...
            if syncing_text.status == STARTED:
                # update params
                pass
            
            # if syncing_text is stopping this frame...
            if syncing_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > syncing_text.tStartRefresh + 6.25-frameTolerance:
                    # keep track of stop time/frame for later
                    syncing_text.tStop = t  # not accounting for scr refresh
                    syncing_text.tStopRefresh = tThisFlipGlobal  # on global time
                    syncing_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'syncing_text.stopped')
                    # update status
                    syncing_text.status = FINISHED
                    syncing_text.setAutoDraw(False)
            
            # *text_0* updates
            
            # if text_0 is starting this frame...
            if text_0.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                text_0.frameNStart = frameN  # exact frame index
                text_0.tStart = t  # local t and not account for scr refresh
                text_0.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_0, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_0.started')
                # update status
                text_0.status = STARTED
                text_0.setAutoDraw(True)
            
            # if text_0 is active this frame...
            if text_0.status == STARTED:
                # update params
                pass
            
            # if text_0 is stopping this frame...
            if text_0.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_0.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_0.tStop = t  # not accounting for scr refresh
                    text_0.tStopRefresh = tThisFlipGlobal  # on global time
                    text_0.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_0.stopped')
                    # update status
                    text_0.status = FINISHED
                    text_0.setAutoDraw(False)
            
            # *Transparent* updates
            
            # if Transparent is starting this frame...
            if Transparent.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                Transparent.frameNStart = frameN  # exact frame index
                Transparent.tStart = t  # local t and not account for scr refresh
                Transparent.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Transparent, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Transparent.started')
                # update status
                Transparent.status = STARTED
                Transparent.setAutoDraw(True)
            
            # if Transparent is active this frame...
            if Transparent.status == STARTED:
                # update params
                pass
            
            # if Transparent is stopping this frame...
            if Transparent.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Transparent.tStartRefresh + 6.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Transparent.tStop = t  # not accounting for scr refresh
                    Transparent.tStopRefresh = tThisFlipGlobal  # on global time
                    Transparent.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Transparent.stopped')
                    # update status
                    Transparent.status = FINISHED
                    Transparent.setAutoDraw(False)
            
            # *Loading_25* updates
            
            # if Loading_25 is starting this frame...
            if Loading_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
                # keep track of start time/frame for later
                Loading_25.frameNStart = frameN  # exact frame index
                Loading_25.tStart = t  # local t and not account for scr refresh
                Loading_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Loading_25, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_25.started')
                # update status
                Loading_25.status = STARTED
                Loading_25.setAutoDraw(True)
            
            # if Loading_25 is active this frame...
            if Loading_25.status == STARTED:
                # update params
                pass
            
            # if Loading_25 is stopping this frame...
            if Loading_25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Loading_25.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Loading_25.tStop = t  # not accounting for scr refresh
                    Loading_25.tStopRefresh = tThisFlipGlobal  # on global time
                    Loading_25.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Loading_25.stopped')
                    # update status
                    Loading_25.status = FINISHED
                    Loading_25.setAutoDraw(False)
            
            # *text_25* updates
            
            # if text_25 is starting this frame...
            if text_25.status == NOT_STARTED and tThisFlip >= 4.25-frameTolerance:
                # keep track of start time/frame for later
                text_25.frameNStart = frameN  # exact frame index
                text_25.tStart = t  # local t and not account for scr refresh
                text_25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_25.started')
                # update status
                text_25.status = STARTED
                text_25.setAutoDraw(True)
            
            # if text_25 is active this frame...
            if text_25.status == STARTED:
                # update params
                pass
            
            # if text_25 is stopping this frame...
            if text_25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_25.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_25.tStop = t  # not accounting for scr refresh
                    text_25.tStopRefresh = tThisFlipGlobal  # on global time
                    text_25.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_25.stopped')
                    # update status
                    text_25.status = FINISHED
                    text_25.setAutoDraw(False)
            
            # *Loading_50* updates
            
            # if Loading_50 is starting this frame...
            if Loading_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
                # keep track of start time/frame for later
                Loading_50.frameNStart = frameN  # exact frame index
                Loading_50.tStart = t  # local t and not account for scr refresh
                Loading_50.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Loading_50, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_50.started')
                # update status
                Loading_50.status = STARTED
                Loading_50.setAutoDraw(True)
            
            # if Loading_50 is active this frame...
            if Loading_50.status == STARTED:
                # update params
                pass
            
            # if Loading_50 is stopping this frame...
            if Loading_50.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Loading_50.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Loading_50.tStop = t  # not accounting for scr refresh
                    Loading_50.tStopRefresh = tThisFlipGlobal  # on global time
                    Loading_50.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Loading_50.stopped')
                    # update status
                    Loading_50.status = FINISHED
                    Loading_50.setAutoDraw(False)
            
            # *text_50* updates
            
            # if text_50 is starting this frame...
            if text_50.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
                # keep track of start time/frame for later
                text_50.frameNStart = frameN  # exact frame index
                text_50.tStart = t  # local t and not account for scr refresh
                text_50.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_50.started')
                # update status
                text_50.status = STARTED
                text_50.setAutoDraw(True)
            
            # if text_50 is active this frame...
            if text_50.status == STARTED:
                # update params
                pass
            
            # if text_50 is stopping this frame...
            if text_50.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_50.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_50.tStop = t  # not accounting for scr refresh
                    text_50.tStopRefresh = tThisFlipGlobal  # on global time
                    text_50.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_50.stopped')
                    # update status
                    text_50.status = FINISHED
                    text_50.setAutoDraw(False)
            
            # *Loading_75* updates
            
            # if Loading_75 is starting this frame...
            if Loading_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
                # keep track of start time/frame for later
                Loading_75.frameNStart = frameN  # exact frame index
                Loading_75.tStart = t  # local t and not account for scr refresh
                Loading_75.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Loading_75, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_75.started')
                # update status
                Loading_75.status = STARTED
                Loading_75.setAutoDraw(True)
            
            # if Loading_75 is active this frame...
            if Loading_75.status == STARTED:
                # update params
                pass
            
            # if Loading_75 is stopping this frame...
            if Loading_75.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Loading_75.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Loading_75.tStop = t  # not accounting for scr refresh
                    Loading_75.tStopRefresh = tThisFlipGlobal  # on global time
                    Loading_75.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Loading_75.stopped')
                    # update status
                    Loading_75.status = FINISHED
                    Loading_75.setAutoDraw(False)
            
            # *text_75* updates
            
            # if text_75 is starting this frame...
            if text_75.status == NOT_STARTED and tThisFlip >= 6.75-frameTolerance:
                # keep track of start time/frame for later
                text_75.frameNStart = frameN  # exact frame index
                text_75.tStart = t  # local t and not account for scr refresh
                text_75.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_75, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_75.started')
                # update status
                text_75.status = STARTED
                text_75.setAutoDraw(True)
            
            # if text_75 is active this frame...
            if text_75.status == STARTED:
                # update params
                pass
            
            # if text_75 is stopping this frame...
            if text_75.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_75.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_75.tStop = t  # not accounting for scr refresh
                    text_75.tStopRefresh = tThisFlipGlobal  # on global time
                    text_75.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_75.stopped')
                    # update status
                    text_75.status = FINISHED
                    text_75.setAutoDraw(False)
            
            # *Loading_100* updates
            
            # if Loading_100 is starting this frame...
            if Loading_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                Loading_100.frameNStart = frameN  # exact frame index
                Loading_100.tStart = t  # local t and not account for scr refresh
                Loading_100.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Loading_100, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Loading_100.started')
                # update status
                Loading_100.status = STARTED
                Loading_100.setAutoDraw(True)
            
            # if Loading_100 is active this frame...
            if Loading_100.status == STARTED:
                # update params
                pass
            
            # if Loading_100 is stopping this frame...
            if Loading_100.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Loading_100.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    Loading_100.tStop = t  # not accounting for scr refresh
                    Loading_100.tStopRefresh = tThisFlipGlobal  # on global time
                    Loading_100.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Loading_100.stopped')
                    # update status
                    Loading_100.status = FINISHED
                    Loading_100.setAutoDraw(False)
            
            # *text_100* updates
            
            # if text_100 is starting this frame...
            if text_100.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
                # keep track of start time/frame for later
                text_100.frameNStart = frameN  # exact frame index
                text_100.tStart = t  # local t and not account for scr refresh
                text_100.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_100, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_100.started')
                # update status
                text_100.status = STARTED
                text_100.setAutoDraw(True)
            
            # if text_100 is active this frame...
            if text_100.status == STARTED:
                # update params
                pass
            
            # if text_100 is stopping this frame...
            if text_100.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_100.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_100.tStop = t  # not accounting for scr refresh
                    text_100.tStopRefresh = tThisFlipGlobal  # on global time
                    text_100.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_100.stopped')
                    # update status
                    text_100.status = FINISHED
                    text_100.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WaitingToMatchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "WaitingToMatch" ---
        for thisComponent in WaitingToMatchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('WaitingToMatch.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-9.250000)
        
        # --- Prepare to start Routine "Partner_Match" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Partner_Match.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from showpartnermatch
        if TrialNumber not in [1, 31, 61]: # establishes two blocks per 32 trials
            continueRoutine = False # if not trial 31 or 63, skip routine completely
        Youhavematched.setText(partnermatch)
        partneremoji_image.setImage(partneravatar)
        # create starting attributes for endpartnermatch_keys
        endpartnermatch_keys.keys = []
        endpartnermatch_keys.rt = []
        _endpartnermatch_keys_allKeys = []
        # keep track of which components have finished
        Partner_MatchComponents = [Youhavematched, partneremoji_image, endpartnermatch_keys, PressToContinue]
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
        frameN = -1
        
        # --- Run Routine "Partner_Match" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Youhavematched* updates
            
            # if Youhavematched is starting this frame...
            if Youhavematched.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Youhavematched.frameNStart = frameN  # exact frame index
                Youhavematched.tStart = t  # local t and not account for scr refresh
                Youhavematched.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Youhavematched, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Youhavematched.started')
                # update status
                Youhavematched.status = STARTED
                Youhavematched.setAutoDraw(True)
            
            # if Youhavematched is active this frame...
            if Youhavematched.status == STARTED:
                # update params
                pass
            
            # *partneremoji_image* updates
            
            # if partneremoji_image is starting this frame...
            if partneremoji_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                partneremoji_image.frameNStart = frameN  # exact frame index
                partneremoji_image.tStart = t  # local t and not account for scr refresh
                partneremoji_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(partneremoji_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'partneremoji_image.started')
                # update status
                partneremoji_image.status = STARTED
                partneremoji_image.setAutoDraw(True)
            
            # if partneremoji_image is active this frame...
            if partneremoji_image.status == STARTED:
                # update params
                pass
            
            # *endpartnermatch_keys* updates
            waitOnFlip = False
            
            # if endpartnermatch_keys is starting this frame...
            if endpartnermatch_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                endpartnermatch_keys.frameNStart = frameN  # exact frame index
                endpartnermatch_keys.tStart = t  # local t and not account for scr refresh
                endpartnermatch_keys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(endpartnermatch_keys, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'endpartnermatch_keys.started')
                # update status
                endpartnermatch_keys.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(endpartnermatch_keys.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(endpartnermatch_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if endpartnermatch_keys.status == STARTED and not waitOnFlip:
                theseKeys = endpartnermatch_keys.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _endpartnermatch_keys_allKeys.extend(theseKeys)
                if len(_endpartnermatch_keys_allKeys):
                    endpartnermatch_keys.keys = _endpartnermatch_keys_allKeys[-1].name  # just the last key pressed
                    endpartnermatch_keys.rt = _endpartnermatch_keys_allKeys[-1].rt
                    endpartnermatch_keys.duration = _endpartnermatch_keys_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *PressToContinue* updates
            
            # if PressToContinue is starting this frame...
            if PressToContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PressToContinue.frameNStart = frameN  # exact frame index
                PressToContinue.tStart = t  # local t and not account for scr refresh
                PressToContinue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PressToContinue, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'PressToContinue.started')
                # update status
                PressToContinue.status = STARTED
                PressToContinue.setAutoDraw(True)
            
            # if PressToContinue is active this frame...
            if PressToContinue.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Partner_MatchComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Partner_Match" ---
        for thisComponent in Partner_MatchComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Partner_Match.stopped', globalClock.getTime(format='float'))
        # check responses
        if endpartnermatch_keys.keys in ['', [], None]:  # No response was made
            endpartnermatch_keys.keys = None
        entiretaskloop.addData('endpartnermatch_keys.keys',endpartnermatch_keys.keys)
        if endpartnermatch_keys.keys != None:  # we had a response
            entiretaskloop.addData('endpartnermatch_keys.rt', endpartnermatch_keys.rt)
            entiretaskloop.addData('endpartnermatch_keys.duration', endpartnermatch_keys.duration)
        # the Routine "Partner_Match" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Photo_Share" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Photo_Share.started', globalClock.getTime(format='float'))
        participantimage_image.setImage(Photos)
        # keep track of which components have finished
        Photo_ShareComponents = [photobeingshared_text, waitforfeedback_text, participantimage_image]
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
        frameN = -1
        
        # --- Run Routine "Photo_Share" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *photobeingshared_text* updates
            
            # if photobeingshared_text is starting this frame...
            if photobeingshared_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                photobeingshared_text.frameNStart = frameN  # exact frame index
                photobeingshared_text.tStart = t  # local t and not account for scr refresh
                photobeingshared_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(photobeingshared_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'photobeingshared_text.started')
                # update status
                photobeingshared_text.status = STARTED
                photobeingshared_text.setAutoDraw(True)
            
            # if photobeingshared_text is active this frame...
            if photobeingshared_text.status == STARTED:
                # update params
                pass
            
            # if photobeingshared_text is stopping this frame...
            if photobeingshared_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > photobeingshared_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    photobeingshared_text.tStop = t  # not accounting for scr refresh
                    photobeingshared_text.tStopRefresh = tThisFlipGlobal  # on global time
                    photobeingshared_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'photobeingshared_text.stopped')
                    # update status
                    photobeingshared_text.status = FINISHED
                    photobeingshared_text.setAutoDraw(False)
            
            # *waitforfeedback_text* updates
            
            # if waitforfeedback_text is starting this frame...
            if waitforfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                waitforfeedback_text.frameNStart = frameN  # exact frame index
                waitforfeedback_text.tStart = t  # local t and not account for scr refresh
                waitforfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(waitforfeedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waitforfeedback_text.started')
                # update status
                waitforfeedback_text.status = STARTED
                waitforfeedback_text.setAutoDraw(True)
            
            # if waitforfeedback_text is active this frame...
            if waitforfeedback_text.status == STARTED:
                # update params
                pass
            
            # if waitforfeedback_text is stopping this frame...
            if waitforfeedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > waitforfeedback_text.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    waitforfeedback_text.tStop = t  # not accounting for scr refresh
                    waitforfeedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    waitforfeedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'waitforfeedback_text.stopped')
                    # update status
                    waitforfeedback_text.status = FINISHED
                    waitforfeedback_text.setAutoDraw(False)
            
            # *participantimage_image* updates
            
            # if participantimage_image is starting this frame...
            if participantimage_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                participantimage_image.frameNStart = frameN  # exact frame index
                participantimage_image.tStart = t  # local t and not account for scr refresh
                participantimage_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(participantimage_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'participantimage_image.started')
                # update status
                participantimage_image.status = STARTED
                participantimage_image.setAutoDraw(True)
            
            # if participantimage_image is active this frame...
            if participantimage_image.status == STARTED:
                # update params
                pass
            
            # if participantimage_image is stopping this frame...
            if participantimage_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > participantimage_image.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    participantimage_image.tStop = t  # not accounting for scr refresh
                    participantimage_image.tStopRefresh = tThisFlipGlobal  # on global time
                    participantimage_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'participantimage_image.stopped')
                    # update status
                    participantimage_image.status = FINISHED
                    participantimage_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Photo_ShareComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Photo_Share" ---
        for thisComponent in Photo_ShareComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Photo_Share.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from initiatefeedbackresponses
        feedbackresponses = (f'{Partner} {Feedback} your photo')
        if Feedback == 'liked':
            fdbkimage ='Images/thumbsup.tiff'
        elif Feedback == 'did not like':
            fdbkimage ='Images/thumbsdown.tiff'
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "Waitingforfeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Waitingforfeedback.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        WaitingforfeedbackComponents = [waiting_text]
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
        frameN = -1
        
        # --- Run Routine "Waitingforfeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *waiting_text* updates
            
            # if waiting_text is starting this frame...
            if waiting_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                waiting_text.frameNStart = frameN  # exact frame index
                waiting_text.tStart = t  # local t and not account for scr refresh
                waiting_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(waiting_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'waiting_text.started')
                # update status
                waiting_text.status = STARTED
                waiting_text.setAutoDraw(True)
            
            # if waiting_text is active this frame...
            if waiting_text.status == STARTED:
                # update params
                pass
            
            # if waiting_text is stopping this frame...
            if waiting_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > waiting_text.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    waiting_text.tStop = t  # not accounting for scr refresh
                    waiting_text.tStopRefresh = tThisFlipGlobal  # on global time
                    waiting_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'waiting_text.stopped')
                    # update status
                    waiting_text.status = FINISHED
                    waiting_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WaitingforfeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Waitingforfeedback" ---
        for thisComponent in WaitingforfeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Waitingforfeedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        displayfeedback_text.setText(feedbackresponses)
        fdbkimage_image.setImage(fdbkimage)
        # Run 'Begin Routine' code from initiatelottery_code
        if TrialNumber%5 == 0: # lottery should only appear every 5 trials and not on trial 0 
            startlottery = 1
        else: 
            startlottery = 0
        # keep track of which components have finished
        feedbackComponents = [displayfeedback_text, fdbkimage_image]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *displayfeedback_text* updates
            
            # if displayfeedback_text is starting this frame...
            if displayfeedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displayfeedback_text.frameNStart = frameN  # exact frame index
                displayfeedback_text.tStart = t  # local t and not account for scr refresh
                displayfeedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayfeedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayfeedback_text.started')
                # update status
                displayfeedback_text.status = STARTED
                displayfeedback_text.setAutoDraw(True)
            
            # if displayfeedback_text is active this frame...
            if displayfeedback_text.status == STARTED:
                # update params
                pass
            
            # if displayfeedback_text is stopping this frame...
            if displayfeedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > displayfeedback_text.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    displayfeedback_text.tStop = t  # not accounting for scr refresh
                    displayfeedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    displayfeedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'displayfeedback_text.stopped')
                    # update status
                    displayfeedback_text.status = FINISHED
                    displayfeedback_text.setAutoDraw(False)
            
            # *fdbkimage_image* updates
            
            # if fdbkimage_image is starting this frame...
            if fdbkimage_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fdbkimage_image.frameNStart = frameN  # exact frame index
                fdbkimage_image.tStart = t  # local t and not account for scr refresh
                fdbkimage_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fdbkimage_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fdbkimage_image.started')
                # update status
                fdbkimage_image.status = STARTED
                fdbkimage_image.setAutoDraw(True)
            
            # if fdbkimage_image is active this frame...
            if fdbkimage_image.status == STARTED:
                # update params
                pass
            
            # if fdbkimage_image is stopping this frame...
            if fdbkimage_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fdbkimage_image.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    fdbkimage_image.tStop = t  # not accounting for scr refresh
                    fdbkimage_image.tStopRefresh = tThisFlipGlobal  # on global time
                    fdbkimage_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fdbkimage_image.stopped')
                    # update status
                    fdbkimage_image.status = FINISHED
                    fdbkimage_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.000000)
        
        # --- Prepare to start Routine "continuesharing" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('continuesharing.started', globalClock.getTime(format='float'))
        # create starting attributes for sharenextphoto_key
        sharenextphoto_key.keys = []
        sharenextphoto_key.rt = []
        _sharenextphoto_key_allKeys = []
        # Run 'Begin Routine' code from hidecontinuesharingroutine_code
        if startlottery == 1:
            continueRoutine = False
        else:
            continueRoutine = True 
        # keep track of which components have finished
        continuesharingComponents = [presstosharenextphoto_text, sharenextphoto_key]
        for thisComponent in continuesharingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "continuesharing" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *presstosharenextphoto_text* updates
            
            # if presstosharenextphoto_text is starting this frame...
            if presstosharenextphoto_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                presstosharenextphoto_text.frameNStart = frameN  # exact frame index
                presstosharenextphoto_text.tStart = t  # local t and not account for scr refresh
                presstosharenextphoto_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(presstosharenextphoto_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'presstosharenextphoto_text.started')
                # update status
                presstosharenextphoto_text.status = STARTED
                presstosharenextphoto_text.setAutoDraw(True)
            
            # if presstosharenextphoto_text is active this frame...
            if presstosharenextphoto_text.status == STARTED:
                # update params
                pass
            
            # *sharenextphoto_key* updates
            waitOnFlip = False
            
            # if sharenextphoto_key is starting this frame...
            if sharenextphoto_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sharenextphoto_key.frameNStart = frameN  # exact frame index
                sharenextphoto_key.tStart = t  # local t and not account for scr refresh
                sharenextphoto_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sharenextphoto_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sharenextphoto_key.started')
                # update status
                sharenextphoto_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(sharenextphoto_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(sharenextphoto_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if sharenextphoto_key.status == STARTED and not waitOnFlip:
                theseKeys = sharenextphoto_key.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _sharenextphoto_key_allKeys.extend(theseKeys)
                if len(_sharenextphoto_key_allKeys):
                    sharenextphoto_key.keys = _sharenextphoto_key_allKeys[0].name  # just the first key pressed
                    sharenextphoto_key.rt = _sharenextphoto_key_allKeys[0].rt
                    sharenextphoto_key.duration = _sharenextphoto_key_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in continuesharingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "continuesharing" ---
        for thisComponent in continuesharingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('continuesharing.stopped', globalClock.getTime(format='float'))
        # check responses
        if sharenextphoto_key.keys in ['', [], None]:  # No response was made
            sharenextphoto_key.keys = None
        entiretaskloop.addData('sharenextphoto_key.keys',sharenextphoto_key.keys)
        if sharenextphoto_key.keys != None:  # we had a response
            entiretaskloop.addData('sharenextphoto_key.rt', sharenextphoto_key.rt)
            entiretaskloop.addData('sharenextphoto_key.duration', sharenextphoto_key.duration)
        # the Routine "continuesharing" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        lotteryloop = data.TrialHandler(nReps=startlottery, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='lotteryloop')
        thisExp.addLoop(lotteryloop)  # add the loop to the experiment
        thisLotteryloop = lotteryloop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLotteryloop.rgb)
        if thisLotteryloop != None:
            for paramName in thisLotteryloop:
                globals()[paramName] = thisLotteryloop[paramName]
        
        for thisLotteryloop in lotteryloop:
            currentLoop = lotteryloop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisLotteryloop.rgb)
            if thisLotteryloop != None:
                for paramName in thisLotteryloop:
                    globals()[paramName] = thisLotteryloop[paramName]
            
            # --- Prepare to start Routine "Choice" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Choice.started', globalClock.getTime(format='float'))
            # create starting attributes for choice_keys
            choice_keys.keys = []
            choice_keys.rt = []
            _choice_keys_allKeys = []
            # keep track of which components have finished
            ChoiceComponents = [lotterychoice_text, computer_text, self_text, choice_keys]
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
            frameN = -1
            
            # --- Run Routine "Choice" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *lotterychoice_text* updates
                
                # if lotterychoice_text is starting this frame...
                if lotterychoice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    lotterychoice_text.frameNStart = frameN  # exact frame index
                    lotterychoice_text.tStart = t  # local t and not account for scr refresh
                    lotterychoice_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(lotterychoice_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'lotterychoice_text.started')
                    # update status
                    lotterychoice_text.status = STARTED
                    lotterychoice_text.setAutoDraw(True)
                
                # if lotterychoice_text is active this frame...
                if lotterychoice_text.status == STARTED:
                    # update params
                    pass
                
                # if lotterychoice_text is stopping this frame...
                if lotterychoice_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > lotterychoice_text.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        lotterychoice_text.tStop = t  # not accounting for scr refresh
                        lotterychoice_text.tStopRefresh = tThisFlipGlobal  # on global time
                        lotterychoice_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'lotterychoice_text.stopped')
                        # update status
                        lotterychoice_text.status = FINISHED
                        lotterychoice_text.setAutoDraw(False)
                
                # *computer_text* updates
                
                # if computer_text is starting this frame...
                if computer_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    computer_text.frameNStart = frameN  # exact frame index
                    computer_text.tStart = t  # local t and not account for scr refresh
                    computer_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(computer_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'computer_text.started')
                    # update status
                    computer_text.status = STARTED
                    computer_text.setAutoDraw(True)
                
                # if computer_text is active this frame...
                if computer_text.status == STARTED:
                    # update params
                    pass
                
                # if computer_text is stopping this frame...
                if computer_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > computer_text.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        computer_text.tStop = t  # not accounting for scr refresh
                        computer_text.tStopRefresh = tThisFlipGlobal  # on global time
                        computer_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'computer_text.stopped')
                        # update status
                        computer_text.status = FINISHED
                        computer_text.setAutoDraw(False)
                
                # *self_text* updates
                
                # if self_text is starting this frame...
                if self_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    self_text.frameNStart = frameN  # exact frame index
                    self_text.tStart = t  # local t and not account for scr refresh
                    self_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(self_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'self_text.started')
                    # update status
                    self_text.status = STARTED
                    self_text.setAutoDraw(True)
                
                # if self_text is active this frame...
                if self_text.status == STARTED:
                    # update params
                    pass
                
                # if self_text is stopping this frame...
                if self_text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > self_text.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        self_text.tStop = t  # not accounting for scr refresh
                        self_text.tStopRefresh = tThisFlipGlobal  # on global time
                        self_text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'self_text.stopped')
                        # update status
                        self_text.status = FINISHED
                        self_text.setAutoDraw(False)
                # Run 'Each Frame' code from setvariables_code
                #import random
                random_entry = random.choice(computer_choice)
                
                # *choice_keys* updates
                waitOnFlip = False
                
                # if choice_keys is starting this frame...
                if choice_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    choice_keys.frameNStart = frameN  # exact frame index
                    choice_keys.tStart = t  # local t and not account for scr refresh
                    choice_keys.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(choice_keys, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'choice_keys.started')
                    # update status
                    choice_keys.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(choice_keys.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(choice_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if choice_keys is stopping this frame...
                if choice_keys.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > choice_keys.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        choice_keys.tStop = t  # not accounting for scr refresh
                        choice_keys.tStopRefresh = tThisFlipGlobal  # on global time
                        choice_keys.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'choice_keys.stopped')
                        # update status
                        choice_keys.status = FINISHED
                        choice_keys.status = FINISHED
                if choice_keys.status == STARTED and not waitOnFlip:
                    theseKeys = choice_keys.getKeys(keyList=['c','s'], ignoreKeys=["escape"], waitRelease=False)
                    _choice_keys_allKeys.extend(theseKeys)
                    if len(_choice_keys_allKeys):
                        choice_keys.keys = _choice_keys_allKeys[-1].name  # just the last key pressed
                        choice_keys.rt = _choice_keys_allKeys[-1].rt
                        choice_keys.duration = _choice_keys_allKeys[-1].duration
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ChoiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Choice" ---
            for thisComponent in ChoiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Choice.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from setvariables_code
            if choice_keys.keys == 'c':
                selfrunOrNot = 0
                comprunOrNot = 1
            elif choice_keys.keys == 's':
                selfrunOrNot = 1
                comprunOrNot = 0
            else:
                selfrunOrNot = 0
                comprunOrNot = 0
            # check responses
            if choice_keys.keys in ['', [], None]:  # No response was made
                choice_keys.keys = None
            lotteryloop.addData('choice_keys.keys',choice_keys.keys)
            if choice_keys.keys != None:  # we had a response
                lotteryloop.addData('choice_keys.rt', choice_keys.rt)
                lotteryloop.addData('choice_keys.duration', choice_keys.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # set up handler to look after randomisation of conditions etc
            computerchoice = data.TrialHandler(nReps=comprunOrNot, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='computerchoice')
            thisExp.addLoop(computerchoice)  # add the loop to the experiment
            thisComputerchoice = computerchoice.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisComputerchoice.rgb)
            if thisComputerchoice != None:
                for paramName in thisComputerchoice:
                    globals()[paramName] = thisComputerchoice[paramName]
            
            for thisComputerchoice in computerchoice:
                currentLoop = computerchoice
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisComputerchoice.rgb)
                if thisComputerchoice != None:
                    for paramName in thisComputerchoice:
                        globals()[paramName] = thisComputerchoice[paramName]
                
                # --- Prepare to start Routine "Lotterycomputerchoice" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Lotterycomputerchoice.started', globalClock.getTime(format='float'))
                # Run 'Begin Routine' code from skipcomputerchoice_code
                #if choice_keys == 's':
                    #continueRoutine = False
                #else:
                    #continueRoutine = True
                response_msg = (f'The computer has chosen {random_entry}.')
                
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
                frameN = -1
                
                # --- Run Routine "Lotterycomputerchoice" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 6.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *lotterycard* updates
                    
                    # if lotterycard is starting this frame...
                    if lotterycard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        lotterycard.frameNStart = frameN  # exact frame index
                        lotterycard.tStart = t  # local t and not account for scr refresh
                        lotterycard.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(lotterycard, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'lotterycard.started')
                        # update status
                        lotterycard.status = STARTED
                        lotterycard.setAutoDraw(True)
                    
                    # if lotterycard is active this frame...
                    if lotterycard.status == STARTED:
                        # update params
                        pass
                    
                    # if lotterycard is stopping this frame...
                    if lotterycard.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > lotterycard.tStartRefresh + 6-frameTolerance:
                            # keep track of stop time/frame for later
                            lotterycard.tStop = t  # not accounting for scr refresh
                            lotterycard.tStopRefresh = tThisFlipGlobal  # on global time
                            lotterycard.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'lotterycard.stopped')
                            # update status
                            lotterycard.status = FINISHED
                            lotterycard.setAutoDraw(False)
                    
                    # *Block1_facedowncard* updates
                    
                    # if Block1_facedowncard is starting this frame...
                    if Block1_facedowncard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        Block1_facedowncard.frameNStart = frameN  # exact frame index
                        Block1_facedowncard.tStart = t  # local t and not account for scr refresh
                        Block1_facedowncard.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(Block1_facedowncard, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Block1_facedowncard.started')
                        # update status
                        Block1_facedowncard.status = STARTED
                        Block1_facedowncard.setAutoDraw(True)
                    
                    # if Block1_facedowncard is active this frame...
                    if Block1_facedowncard.status == STARTED:
                        # update params
                        pass
                    
                    # if Block1_facedowncard is stopping this frame...
                    if Block1_facedowncard.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > Block1_facedowncard.tStartRefresh + 6-frameTolerance:
                            # keep track of stop time/frame for later
                            Block1_facedowncard.tStop = t  # not accounting for scr refresh
                            Block1_facedowncard.tStopRefresh = tThisFlipGlobal  # on global time
                            Block1_facedowncard.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'Block1_facedowncard.stopped')
                            # update status
                            Block1_facedowncard.status = FINISHED
                            Block1_facedowncard.setAutoDraw(False)
                    
                    # *computerresponse* updates
                    
                    # if computerresponse is starting this frame...
                    if computerresponse.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                        # keep track of start time/frame for later
                        computerresponse.frameNStart = frameN  # exact frame index
                        computerresponse.tStart = t  # local t and not account for scr refresh
                        computerresponse.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(computerresponse, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'computerresponse.started')
                        # update status
                        computerresponse.status = STARTED
                        computerresponse.setAutoDraw(True)
                    
                    # if computerresponse is active this frame...
                    if computerresponse.status == STARTED:
                        # update params
                        pass
                    
                    # if computerresponse is stopping this frame...
                    if computerresponse.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > computerresponse.tStartRefresh + 4-frameTolerance:
                            # keep track of stop time/frame for later
                            computerresponse.tStop = t  # not accounting for scr refresh
                            computerresponse.tStopRefresh = tThisFlipGlobal  # on global time
                            computerresponse.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'computerresponse.stopped')
                            # update status
                            computerresponse.status = FINISHED
                            computerresponse.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in LotterycomputerchoiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Lotterycomputerchoice" ---
                for thisComponent in LotterycomputerchoiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Lotterycomputerchoice.stopped', globalClock.getTime(format='float'))
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-6.000000)
            # completed comprunOrNot repeats of 'computerchoice'
            
            
            # set up handler to look after randomisation of conditions etc
            selfchoice = data.TrialHandler(nReps=selfrunOrNot, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='selfchoice')
            thisExp.addLoop(selfchoice)  # add the loop to the experiment
            thisSelfchoice = selfchoice.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisSelfchoice.rgb)
            if thisSelfchoice != None:
                for paramName in thisSelfchoice:
                    globals()[paramName] = thisSelfchoice[paramName]
            
            for thisSelfchoice in selfchoice:
                currentLoop = selfchoice
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisSelfchoice.rgb)
                if thisSelfchoice != None:
                    for paramName in thisSelfchoice:
                        globals()[paramName] = thisSelfchoice[paramName]
                
                # --- Prepare to start Routine "Lotteryselfchoice" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('Lotteryselfchoice.started', globalClock.getTime(format='float'))
                # Run 'Begin Routine' code from skipselfchoice_code_2
                #if choice_keys == 'c':
                    #continueRoutine = False
                #else:
                    #continueRoutine = True
                # create starting attributes for lotteryguess_keys
                lotteryguess_keys.keys = []
                lotteryguess_keys.rt = []
                _lotteryguess_keys_allKeys = []
                responsefeedback.setText(feedback_msg)
                # keep track of which components have finished
                LotteryselfchoiceComponents = [pickacard_text, higher_text, lower_text, lotteryguess_keys, responsefeedback, block1_cardimage]
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
                frameN = -1
                
                # --- Run Routine "Lotteryselfchoice" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 8.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *pickacard_text* updates
                    
                    # if pickacard_text is starting this frame...
                    if pickacard_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        pickacard_text.frameNStart = frameN  # exact frame index
                        pickacard_text.tStart = t  # local t and not account for scr refresh
                        pickacard_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(pickacard_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'pickacard_text.started')
                        # update status
                        pickacard_text.status = STARTED
                        pickacard_text.setAutoDraw(True)
                    
                    # if pickacard_text is active this frame...
                    if pickacard_text.status == STARTED:
                        # update params
                        pass
                    
                    # if pickacard_text is stopping this frame...
                    if pickacard_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > pickacard_text.tStartRefresh + 8-frameTolerance:
                            # keep track of stop time/frame for later
                            pickacard_text.tStop = t  # not accounting for scr refresh
                            pickacard_text.tStopRefresh = tThisFlipGlobal  # on global time
                            pickacard_text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'pickacard_text.stopped')
                            # update status
                            pickacard_text.status = FINISHED
                            pickacard_text.setAutoDraw(False)
                    
                    # *higher_text* updates
                    
                    # if higher_text is starting this frame...
                    if higher_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        higher_text.frameNStart = frameN  # exact frame index
                        higher_text.tStart = t  # local t and not account for scr refresh
                        higher_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(higher_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'higher_text.started')
                        # update status
                        higher_text.status = STARTED
                        higher_text.setAutoDraw(True)
                    
                    # if higher_text is active this frame...
                    if higher_text.status == STARTED:
                        # update params
                        pass
                    
                    # if higher_text is stopping this frame...
                    if higher_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > higher_text.tStartRefresh + 8-frameTolerance:
                            # keep track of stop time/frame for later
                            higher_text.tStop = t  # not accounting for scr refresh
                            higher_text.tStopRefresh = tThisFlipGlobal  # on global time
                            higher_text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'higher_text.stopped')
                            # update status
                            higher_text.status = FINISHED
                            higher_text.setAutoDraw(False)
                    
                    # *lower_text* updates
                    
                    # if lower_text is starting this frame...
                    if lower_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        lower_text.frameNStart = frameN  # exact frame index
                        lower_text.tStart = t  # local t and not account for scr refresh
                        lower_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(lower_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'lower_text.started')
                        # update status
                        lower_text.status = STARTED
                        lower_text.setAutoDraw(True)
                    
                    # if lower_text is active this frame...
                    if lower_text.status == STARTED:
                        # update params
                        pass
                    
                    # if lower_text is stopping this frame...
                    if lower_text.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > lower_text.tStartRefresh + 8-frameTolerance:
                            # keep track of stop time/frame for later
                            lower_text.tStop = t  # not accounting for scr refresh
                            lower_text.tStopRefresh = tThisFlipGlobal  # on global time
                            lower_text.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'lower_text.stopped')
                            # update status
                            lower_text.status = FINISHED
                            lower_text.setAutoDraw(False)
                    
                    # *lotteryguess_keys* updates
                    waitOnFlip = False
                    
                    # if lotteryguess_keys is starting this frame...
                    if lotteryguess_keys.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                        # keep track of start time/frame for later
                        lotteryguess_keys.frameNStart = frameN  # exact frame index
                        lotteryguess_keys.tStart = t  # local t and not account for scr refresh
                        lotteryguess_keys.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(lotteryguess_keys, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'lotteryguess_keys.started')
                        # update status
                        lotteryguess_keys.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(lotteryguess_keys.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(lotteryguess_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if lotteryguess_keys is stopping this frame...
                    if lotteryguess_keys.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > lotteryguess_keys.tStartRefresh + 3-frameTolerance:
                            # keep track of stop time/frame for later
                            lotteryguess_keys.tStop = t  # not accounting for scr refresh
                            lotteryguess_keys.tStopRefresh = tThisFlipGlobal  # on global time
                            lotteryguess_keys.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'lotteryguess_keys.stopped')
                            # update status
                            lotteryguess_keys.status = FINISHED
                            lotteryguess_keys.status = FINISHED
                    if lotteryguess_keys.status == STARTED and not waitOnFlip:
                        theseKeys = lotteryguess_keys.getKeys(keyList=['h','l'], ignoreKeys=["escape"], waitRelease=False)
                        _lotteryguess_keys_allKeys.extend(theseKeys)
                        if len(_lotteryguess_keys_allKeys):
                            lotteryguess_keys.keys = _lotteryguess_keys_allKeys[0].name  # just the first key pressed
                            lotteryguess_keys.rt = _lotteryguess_keys_allKeys[0].rt
                            lotteryguess_keys.duration = _lotteryguess_keys_allKeys[0].duration
                    # Run 'Each Frame' code from displaylotterychoice_code
                    if lotteryguess_keys.keys == 'l':
                        feedback_msg = (f'You have chosen lower.')
                    elif lotteryguess_keys.keys == 'h':
                        feedback_msg = (f'You have chosen higher.')
                    else:
                        feedback_msg = (f'No response recorded.')
                    
                    responsefeedback.setText(feedback_msg)
                    
                    
                    # *responsefeedback* updates
                    
                    # if responsefeedback is starting this frame...
                    if responsefeedback.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                        # keep track of start time/frame for later
                        responsefeedback.frameNStart = frameN  # exact frame index
                        responsefeedback.tStart = t  # local t and not account for scr refresh
                        responsefeedback.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(responsefeedback, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'responsefeedback.started')
                        # update status
                        responsefeedback.status = STARTED
                        responsefeedback.setAutoDraw(True)
                    
                    # if responsefeedback is active this frame...
                    if responsefeedback.status == STARTED:
                        # update params
                        pass
                    
                    # if responsefeedback is stopping this frame...
                    if responsefeedback.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > responsefeedback.tStartRefresh + 4-frameTolerance:
                            # keep track of stop time/frame for later
                            responsefeedback.tStop = t  # not accounting for scr refresh
                            responsefeedback.tStopRefresh = tThisFlipGlobal  # on global time
                            responsefeedback.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'responsefeedback.stopped')
                            # update status
                            responsefeedback.status = FINISHED
                            responsefeedback.setAutoDraw(False)
                    
                    # *block1_cardimage* updates
                    
                    # if block1_cardimage is starting this frame...
                    if block1_cardimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        block1_cardimage.frameNStart = frameN  # exact frame index
                        block1_cardimage.tStart = t  # local t and not account for scr refresh
                        block1_cardimage.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(block1_cardimage, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'block1_cardimage.started')
                        # update status
                        block1_cardimage.status = STARTED
                        block1_cardimage.setAutoDraw(True)
                    
                    # if block1_cardimage is active this frame...
                    if block1_cardimage.status == STARTED:
                        # update params
                        pass
                    
                    # if block1_cardimage is stopping this frame...
                    if block1_cardimage.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > block1_cardimage.tStartRefresh + 8-frameTolerance:
                            # keep track of stop time/frame for later
                            block1_cardimage.tStop = t  # not accounting for scr refresh
                            block1_cardimage.tStopRefresh = tThisFlipGlobal  # on global time
                            block1_cardimage.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'block1_cardimage.stopped')
                            # update status
                            block1_cardimage.status = FINISHED
                            block1_cardimage.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in LotteryselfchoiceComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "Lotteryselfchoice" ---
                for thisComponent in LotteryselfchoiceComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('Lotteryselfchoice.stopped', globalClock.getTime(format='float'))
                # check responses
                if lotteryguess_keys.keys in ['', [], None]:  # No response was made
                    lotteryguess_keys.keys = None
                selfchoice.addData('lotteryguess_keys.keys',lotteryguess_keys.keys)
                if lotteryguess_keys.keys != None:  # we had a response
                    selfchoice.addData('lotteryguess_keys.rt', lotteryguess_keys.rt)
                    selfchoice.addData('lotteryguess_keys.duration', lotteryguess_keys.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-8.000000)
            # completed selfrunOrNot repeats of 'selfchoice'
            
            
            # --- Prepare to start Routine "Continue" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('Continue.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from code
            if TrialNumber%30 == 0: # needs to be set to 30 for actual run of task
                continueRoutine = False # if not trial 31 or 61, or 91 skip routine completely
            if comprunOrNot ==0 and selfrunOrNot == 0:
                resumetext = 'You missed an opportunity to play the lottery. \n\n\n Please respond withtin 3 seconds on your next opportunity. \n\nPress space to continue.'
            else:
                resumetext = 'Press space to resume sharing your photos.'
            # create starting attributes for resumeafterlottery_keys
            resumeafterlottery_keys.keys = []
            resumeafterlottery_keys.rt = []
            _resumeafterlottery_keys_allKeys = []
            resumetext_text.setText(resumetext)
            # keep track of which components have finished
            ContinueComponents = [resumeafterlottery_keys, resumetext_text]
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
            frameN = -1
            
            # --- Run Routine "Continue" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *resumeafterlottery_keys* updates
                waitOnFlip = False
                
                # if resumeafterlottery_keys is starting this frame...
                if resumeafterlottery_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resumeafterlottery_keys.frameNStart = frameN  # exact frame index
                    resumeafterlottery_keys.tStart = t  # local t and not account for scr refresh
                    resumeafterlottery_keys.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resumeafterlottery_keys, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resumeafterlottery_keys.started')
                    # update status
                    resumeafterlottery_keys.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(resumeafterlottery_keys.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(resumeafterlottery_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if resumeafterlottery_keys.status == STARTED and not waitOnFlip:
                    theseKeys = resumeafterlottery_keys.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _resumeafterlottery_keys_allKeys.extend(theseKeys)
                    if len(_resumeafterlottery_keys_allKeys):
                        resumeafterlottery_keys.keys = _resumeafterlottery_keys_allKeys[0].name  # just the first key pressed
                        resumeafterlottery_keys.rt = _resumeafterlottery_keys_allKeys[0].rt
                        resumeafterlottery_keys.duration = _resumeafterlottery_keys_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *resumetext_text* updates
                
                # if resumetext_text is starting this frame...
                if resumetext_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resumetext_text.frameNStart = frameN  # exact frame index
                    resumetext_text.tStart = t  # local t and not account for scr refresh
                    resumetext_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resumetext_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'resumetext_text.started')
                    # update status
                    resumetext_text.status = STARTED
                    resumetext_text.setAutoDraw(True)
                
                # if resumetext_text is active this frame...
                if resumetext_text.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ContinueComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "Continue" ---
            for thisComponent in ContinueComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('Continue.stopped', globalClock.getTime(format='float'))
            # check responses
            if resumeafterlottery_keys.keys in ['', [], None]:  # No response was made
                resumeafterlottery_keys.keys = None
            lotteryloop.addData('resumeafterlottery_keys.keys',resumeafterlottery_keys.keys)
            if resumeafterlottery_keys.keys != None:  # we had a response
                lotteryloop.addData('resumeafterlottery_keys.rt', resumeafterlottery_keys.rt)
                lotteryloop.addData('resumeafterlottery_keys.duration', resumeafterlottery_keys.duration)
            # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed startlottery repeats of 'lotteryloop'
        
        
        # --- Prepare to start Routine "SalienceRating" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('SalienceRating.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from saliencyrating_code
        if not TrialNumber%30 == 0: # establishes two blocks per 32 trials
            continueRoutine = False # if not trial 31 or 63, skip routine completely
        salienceratingtext = (f'How likely are you to share photos with {Partner} in the future? \n\n Use your left and right arrows to move the arrow to your desired rating.' )
        event.clearEvents('keyboard')
        salience_slider.markerPos = 3
        saliencequestion_text.setText(salienceratingtext)
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        salienceavatar_image.setImage(partneravatar)
        displayrating_text.setText(rating_forsalience)
        # keep track of which components have finished
        SalienceRatingComponents = [saliencequestion_text, key_resp, salienceavatar_image, saliencecontinue_text, displayrating_text]
        for thisComponent in SalienceRatingComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SalienceRating" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from saliencyrating_code
            salience_slider.draw()
            keys = event.getKeys()
            displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
            if len(keys):
                if 'left' in keys:
                    salience_slider.markerPos = salience_slider.markerPos - .1
                    rating_forsalience = salience_slider.getRating()
                    displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
                elif 'right' in keys:
                    salience_slider.markerPos = salience_slider.markerPos + .1
                    rating_forsalience = salience_slider.getRating()
                    displayrating_text.setText(round(salience_slider.getMarkerPos(),1))
            
            # *saliencequestion_text* updates
            
            # if saliencequestion_text is starting this frame...
            if saliencequestion_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                saliencequestion_text.frameNStart = frameN  # exact frame index
                saliencequestion_text.tStart = t  # local t and not account for scr refresh
                saliencequestion_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(saliencequestion_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'saliencequestion_text.started')
                # update status
                saliencequestion_text.status = STARTED
                saliencequestion_text.setAutoDraw(True)
            
            # if saliencequestion_text is active this frame...
            if saliencequestion_text.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *salienceavatar_image* updates
            
            # if salienceavatar_image is starting this frame...
            if salienceavatar_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                salienceavatar_image.frameNStart = frameN  # exact frame index
                salienceavatar_image.tStart = t  # local t and not account for scr refresh
                salienceavatar_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(salienceavatar_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'salienceavatar_image.started')
                # update status
                salienceavatar_image.status = STARTED
                salienceavatar_image.setAutoDraw(True)
            
            # if salienceavatar_image is active this frame...
            if salienceavatar_image.status == STARTED:
                # update params
                pass
            
            # *saliencecontinue_text* updates
            
            # if saliencecontinue_text is starting this frame...
            if saliencecontinue_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                saliencecontinue_text.frameNStart = frameN  # exact frame index
                saliencecontinue_text.tStart = t  # local t and not account for scr refresh
                saliencecontinue_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(saliencecontinue_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'saliencecontinue_text.started')
                # update status
                saliencecontinue_text.status = STARTED
                saliencecontinue_text.setAutoDraw(True)
            
            # if saliencecontinue_text is active this frame...
            if saliencecontinue_text.status == STARTED:
                # update params
                pass
            
            # *displayrating_text* updates
            
            # if displayrating_text is starting this frame...
            if displayrating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displayrating_text.frameNStart = frameN  # exact frame index
                displayrating_text.tStart = t  # local t and not account for scr refresh
                displayrating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayrating_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displayrating_text.started')
                # update status
                displayrating_text.status = STARTED
                displayrating_text.setAutoDraw(True)
            
            # if displayrating_text is active this frame...
            if displayrating_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SalienceRatingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SalienceRating" ---
        for thisComponent in SalienceRatingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('SalienceRating.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from saliencyrating_code
        #saliencerating = salience_slider.getRating()
        entiretaskloop.addData('salience_rating', round(salience_slider.getMarkerPos(),1))
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        entiretaskloop.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            entiretaskloop.addData('key_resp.rt', key_resp.rt)
            entiretaskloop.addData('key_resp.duration', key_resp.duration)
        # the Routine "SalienceRating" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "StressLevel" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('StressLevel.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from stresslevelslider
        if not TrialNumber%30 == 0: # establishes two blocks per 32 trials
            continueRoutine = False # if not trial 31 or 63, skip routine completely
        stressleveltext = (f'Please rate your current stress level. \n\n\n Use your mouse or left and right arrows to move the arrow to your desired rating.' )
        event.clearEvents('keyboard')
        stress_slider.markerPos = 5
        
        stresslevel_text.setText(stressleveltext)
        # create starting attributes for stresslevel_keypress
        stresslevel_keypress.keys = []
        stresslevel_keypress.rt = []
        _stresslevel_keypress_allKeys = []
        displaystressrating_text.setText(rating_forstress)
        # keep track of which components have finished
        StressLevelComponents = [stresslevel_text, stresslevel_keypress, displaystressrating_text]
        for thisComponent in StressLevelComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "StressLevel" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from stresslevelslider
            stress_slider.draw()
            keys = event.getKeys()
            displaystressrating_text.setText(round(stress_slider.getMarkerPos(),1))
            if len(keys):
                if 'left' in keys:
                    stress_slider.markerPos = stress_slider.markerPos - .1
                    rating_forstress = stress_slider.getRating()
                    displayrating_text.setText(round(stress_slider.getMarkerPos(),1))
                elif 'right' in keys:
                    stress_slider.markerPos = stress_slider.markerPos + .1
                    rating_forstress = stress_slider.getRating()
                    displayrating_text.setText(round(stress_slider.getMarkerPos(),1))
            
            # *stresslevel_text* updates
            
            # if stresslevel_text is starting this frame...
            if stresslevel_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stresslevel_text.frameNStart = frameN  # exact frame index
                stresslevel_text.tStart = t  # local t and not account for scr refresh
                stresslevel_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stresslevel_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stresslevel_text.started')
                # update status
                stresslevel_text.status = STARTED
                stresslevel_text.setAutoDraw(True)
            
            # if stresslevel_text is active this frame...
            if stresslevel_text.status == STARTED:
                # update params
                pass
            
            # *stresslevel_keypress* updates
            waitOnFlip = False
            
            # if stresslevel_keypress is starting this frame...
            if stresslevel_keypress.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stresslevel_keypress.frameNStart = frameN  # exact frame index
                stresslevel_keypress.tStart = t  # local t and not account for scr refresh
                stresslevel_keypress.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stresslevel_keypress, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stresslevel_keypress.started')
                # update status
                stresslevel_keypress.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(stresslevel_keypress.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(stresslevel_keypress.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if stresslevel_keypress.status == STARTED and not waitOnFlip:
                theseKeys = stresslevel_keypress.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _stresslevel_keypress_allKeys.extend(theseKeys)
                if len(_stresslevel_keypress_allKeys):
                    stresslevel_keypress.keys = _stresslevel_keypress_allKeys[-1].name  # just the last key pressed
                    stresslevel_keypress.rt = _stresslevel_keypress_allKeys[-1].rt
                    stresslevel_keypress.duration = _stresslevel_keypress_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *displaystressrating_text* updates
            
            # if displaystressrating_text is starting this frame...
            if displaystressrating_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displaystressrating_text.frameNStart = frameN  # exact frame index
                displaystressrating_text.tStart = t  # local t and not account for scr refresh
                displaystressrating_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displaystressrating_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'displaystressrating_text.started')
                # update status
                displaystressrating_text.status = STARTED
                displaystressrating_text.setAutoDraw(True)
            
            # if displaystressrating_text is active this frame...
            if displaystressrating_text.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in StressLevelComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "StressLevel" ---
        for thisComponent in StressLevelComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('StressLevel.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from stresslevelslider
        stresslevel = stress_slider.getRating()
        entiretaskloop.addData('stress_level', round(stress_slider.getMarkerPos(),1))
        # check responses
        if stresslevel_keypress.keys in ['', [], None]:  # No response was made
            stresslevel_keypress.keys = None
        entiretaskloop.addData('stresslevel_keypress.keys',stresslevel_keypress.keys)
        if stresslevel_keypress.keys != None:  # we had a response
            entiretaskloop.addData('stresslevel_keypress.rt', stresslevel_keypress.rt)
            entiretaskloop.addData('stresslevel_keypress.duration', stresslevel_keypress.duration)
        # the Routine "StressLevel" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'entiretaskloop'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
