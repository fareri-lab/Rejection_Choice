/******************************
 * Rejectiontask_Oneloop Test *
 ******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'RejTask';  // from the Builder filename that created this script
let expInfo = {
    'participant': ''
};

// add info from the URL:
util.addInfoFromUrl(expInfo);
console.log(expInfo['participant'])
// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from saliencyrating_code
saliencerating = "";
salienceratingtext = "";
rating_forsalience = "";

// Run 'Before Experiment' code from stresslevelslider
stresslevel = "";
stressleveltext = "";
rating_forstress = "";




// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'norm',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Welcome_ScreenRoutineBegin());
flowScheduler.add(Welcome_ScreenRoutineEachFrame());
flowScheduler.add(Welcome_ScreenRoutineEnd());
flowScheduler.add(testRoutineBegin());
flowScheduler.add(testRoutineEachFrame());
flowScheduler.add(testRoutineEnd());
flowScheduler.add(First_InstructionsRoutineBegin());
flowScheduler.add(First_InstructionsRoutineEachFrame());
flowScheduler.add(First_InstructionsRoutineEnd());
const entiretaskloopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(entiretaskloopLoopBegin(entiretaskloopLoopScheduler));
flowScheduler.add(entiretaskloopLoopScheduler);
flowScheduler.add(entiretaskloopLoopEnd);
flowScheduler.add(End_ScreenRoutineBegin());
flowScheduler.add(End_ScreenRoutineEachFrame());
flowScheduler.add(End_ScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo});


psychoJS.start({
  resources: [

    {'name': 'Task_Images/facedown_card.png', 'path': 'Task_Images/facedown_card.png'},
        
        {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_trials.csv`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_trials.csv`},
    {'name': 'Task_Images/facedown_card.png', 'path': 'Task_Images/facedown_card.png'},
    {'name': 'Task_Images/nerdemoji_nobackground.png', 'path': 'Task_Images/nerdemoji_nobackground.png'},
    {'name': 'Task_Images/smilingemoji.png', 'path': 'Task_Images/smilingemoji.png'},
    {'name': 'Task_Images/sunglassemoji_nobackground.png', 'path': 'Task_Images/sunglassemoji_nobackground.png'},
    {'name': 'Task_Images/thumbsdown.png', 'path': 'Task_Images/thumbsdown.png'},
    {'name': 'Task_Images/thumbsup.png', 'path': 'Task_Images/thumbsup.png'},
    {'name': 'Task_Images/cowboyemoji.png', 'path': 'Task_Images/cowboyemoji.png'},
    {'name': 'Task_Images/huggingemoji.png', 'path': 'Task_Images/huggingemoji.png'},

    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_5.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_5.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_13.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_13.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_12.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_12.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_4.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_4.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_6.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_6.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_10.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_10.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_11.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_11.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_7.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_7.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_3.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_3.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_15.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_15.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_29.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_29.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_28.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_28.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_14.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_14.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_2.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_2.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_16.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_16.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_17.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_17.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_1.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_1.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_26.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_26.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_27.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_27.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_19.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_19.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_25.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_25.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_30.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_30.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_24.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_24.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_18.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_18.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_20.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_20.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_21.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_21.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_9.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_9.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_23.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_23.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_22.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_22.jpeg` ,},
    {'name': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg`, 'path': `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_Images/${expInfo["participant"]}_Image_8.jpeg` ,}

]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.1';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);

  return Scheduler.Event.NEXT;
}

var weblink;
weblink= "https://adelphiderner.qualtrics.com/jfe/form/SV_4GR8sO1rBmqsz3M";
var Welcome_ScreenClock;
var Welcome;
var endwelcomescreen_keys;
var partnermatch;
var partneravatar;
var testClock;
var First_InstructionsClock;
var FirstInstructions;
var endinstructionscreen_keys;
var partner_codeClock;
var WaitingToMatchClock;
var Match_text;
var syncing_text;
var text_0;
var Transparent;
var Loading_25;
var text_25;
var Loading_50;
var text_50;
var Loading_75;
var text_75;
var Loading_100;
var text_100;
var Partner_MatchClock;
var Youhavematched;
var partneremoji_image;
var endpartnermatch_keys;
var PressToContinue;
var Photo_ShareClock;
var photobeingshared_text;
var waitforfeedback_text;
var feedbackresponses;
var fdbkimage;
var participantimage_image;
var WaitingforfeedbackClock;
var waiting_text;
var feedbackClock;
var displayfeedback_text;
var fdbkimage_image;
var startlottery;
var continuesharingClock;
var presstosharenextphoto_text;
var sharenextphoto_key;
var ChoiceClock;
var lotterychoice_text;
var computer_text;
var self_text;
var conditionalBlank;
var response_msg;
var feedback_msg;
var computer_choice;
var selfrunOrNot;
var comprunOrNot;
var playlottery;
var resumetext;
var choice_keys;
var LotterycomputerchoiceClock;
var lotterycard;
var Block1_facedowncard;
var computerresponse;
var LotteryselfchoiceClock;
var pickacard_text;
var higher_text;
var lower_text;
var lotteryguess_keys;
var responsefeedback;
var block1_cardimage;
var ContinueClock;
var resumeafterlottery_keys;
var resumetext_text;
var end_screen;
var end_screenclock;
var end_screen_keys;
// var thankyou_screen;
// var thankyou_screenclock;

// salience slider
var userMouse;
var mouseClock;
var SalienceRatingClock;
var salience_slider;
var saliencequestion_text;
var key_resp;
var salienceavatar_image;
var saliencecontinue_text;
var Salience_Button;
var displayrating_text;
var saliencerating;
var salienceratingtext;
var rating_forsalience;

//stress slider
var StressLevelClock;
var stress_slider;
var stresslevel_text;
var userMouse;
var mouseClock;
var Stress_Button;
var stresscontinue_text
var stresslevel_keypress;
var displaystressrating_text;
var globalClock;
var routineTimer;
var stresslevel;
var stressleveltext;
var rating_forstress;
var partnermatch;
var partneravatar;
var feedbackresponses;
var fdbkimage;
var startlottery;
var response_msg;
var feedback_msg;
var computer_choice;
var selfrunOrNot;
var comprunOrNot;
var resumetext;


async function experimentInit() {
  // Initialize components for Routine "Welcome_Screen"
  Welcome_ScreenClock = new util.Clock();
  Welcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'Welcome',
    text: 'Welcome to the Social Media Task!\n\n\nToday you will have the opportunity to share some of your Instagram photos with other participants and receive feedback, as well as a few opportunities to play a lottery for an additional bonus.\n\n\n To begin, you will be assigned a partner at random by the computer. Next, your instagram photos will be shared with your partner. After each photo is shared, your partner will give you feedback on whether they liked or disliked your photo. You will have the chance to share your photos with 3 different partners during this task.\n\n\nPress space to continue.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  endwelcomescreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});


  // Run 'Begin Experiment' code from buildspreadsheet
  partnermatch = "";
  partneravatar = "";

  // Initialize components for Routine "test"
  testClock = new util.Clock();
  // Initialize components for Routine "First_Instructions"
  First_InstructionsClock = new util.Clock();
  FirstInstructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'FirstInstructions',
    text: 'At select times throughout the course of the experiment, you will be asked to play a lottery. \n\n\n During each lottery, the task is to guess if a facedown card is higher or lower than a given number. You can either choose to play the lottery for yourself or have the computer play on your behalf.\n\n\n You will not receive feedback about any of your guesses. However, at the end of the task, one lottery guess will be selected at random and you will be notified of any earnings at the end of the task.\n\n\n You are now ready to begin sharing your photos. \nPress space to begin! \n',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  endinstructionscreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "partner_code"
  partner_codeClock = new util.Clock();
  // Run 'Begin Experiment' code from partnermatchcode

  // Initialize components for Routine "WaitingToMatch"
  WaitingToMatchClock = new util.Clock();
  Match_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Match_text',
    text: 'You will now be matched with a game partner selected at random by the computer. \n\n Please wait...',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  syncing_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'syncing_text',
    text: 'Syncing…',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.3], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0
  });

  text_0 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_0',
    text: '0%',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0
  });

  Transparent = new visual.Rect ({
    win: psychoJS.window, name: 'Transparent',
    width: [1, 0.1][0], height: [1, 0.1][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.2, lineColor: new util.Color('white'),
    fillColor: new util.Color([0.0, 0.0, 0.0]),
    opacity: undefined, depth: -4, interpolate: true,
  });

  Loading_25 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_25',
    width: [0.25, 0.1][0], height: [0.25, 0.1][1],
    ori: 0.0, pos: [(- 0.375), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });

  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: '25%',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0
  });

  Loading_50 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_50',
    width: [0.5, 0.1][0], height: [0.5, 0.1][1],
    ori: 0.0, pos: [(- 0.25), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -7, interpolate: true,
  });

  text_50 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_50',
    text: '50%',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0
  });

  Loading_75 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_75',
    width: [0.75, 0.1][0], height: [0.75, 0.1][1],
    ori: 0.0, pos: [(- 0.125), 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -9, interpolate: true,
  });

  text_75 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_75',
    text: '75%',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0
  });

  Loading_100 = new visual.Rect ({
    win: psychoJS.window, name: 'Loading_100',
    width: [1, 0.1][0], height: [1, 0.1][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -11, interpolate: true,
  });

  text_100 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_100',
    text: '100%',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.2)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -12.0
  });

  // Initialize components for Routine "Partner_Match"
  Partner_MatchClock = new util.Clock();
  Youhavematched = new visual.TextStim({
    win: psychoJS.window,
    name: 'Youhavematched',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.6], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  partneremoji_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'partneremoji_image', units : undefined,
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0
  });
  endpartnermatch_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  PressToContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'PressToContinue',
    text: 'Press space to continue.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.6)], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0
  });

  // Initialize components for Routine "Photo_Share"
  Photo_ShareClock = new util.Clock();
  photobeingshared_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'photobeingshared_text',
    text: 'This photo is now being shared',
    font: 'Open Sans',
    units: undefined,
    pos: [0.0, 0.6], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  waitforfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'waitforfeedback_text',
    text: 'Please wait for feedback.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.6)], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  // Run 'Begin Experiment' code from initiatefeedbackresponses
  feedbackresponses = "";
  fdbkimage = "";

  participantimage_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'participantimage_image', units : undefined,
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0
  });


  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  displayfeedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayfeedback_text',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.75], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  fdbkimage_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fdbkimage_image', units : undefined,
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 1.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0
  });

  // Run 'Begin Experiment' code from initiatelottery_code
  startlottery = "";

  // Initialize components for Routine "continuesharing"
  continuesharingClock = new util.Clock();
  presstosharenextphoto_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'presstosharenextphoto_text',
    text: 'Press space to share your next photo.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  sharenextphoto_key = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "Choice"
  ChoiceClock = new util.Clock();
  lotterychoice_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'lotterychoice_text',
    text: 'You have reached the lottery. Please choose [c] to have the computer play on your behalf or choose [s] to play the lottery for yourself. You have four seconds to choose.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.3], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });

  computer_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'computer_text',
    text: 'Computer',
    font: 'Open Sans',
    units: undefined,
    pos: [(- 0.3), (- 0.4)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  self_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'self_text',
    text: 'Self',
    font: 'Open Sans',
    units: undefined,
    pos: [0.3, (- 0.4)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0
  });

  conditionalBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'conditionalconditionalBlank',
    text: '',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -6.0
  });

  // Run 'Begin Experiment' code from setvariables_code
  response_msg = " ";
  feedback_msg = " ";
  computer_choice = ["lower", "lower", "lower", "lower", "lower", "higher", "higher", "higher", "higher", "higher"];
  selfrunOrNot = "";
  comprunOrNot = "";
  playlottery = "";
  resumetext = "";

  choice_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Initialize components for Routine "Lotterycomputerchoice"
  LotterycomputerchoiceClock = new util.Clock();
  lotterycard = new visual.TextStim({
    win: psychoJS.window,
    name: 'lotterycard',
    text: 'The computer will select whether it believes the card will be higher or lower than 5.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.6], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  Block1_facedowncard = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Block1_facedowncard', units : undefined,
    image : 'Task_Images/facedown_card.png', mask : undefined,
    ori : 0.0, pos : [0, -0.1], size : [0.75, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0
  });
  computerresponse = new visual.TextStim({
    win: psychoJS.window,
    name: 'computerresponse',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.65)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('cornflowerblue'),  opacity: undefined,
    depth: -3.0
  });

  // Initialize components for Routine "Lotteryselfchoice"
  LotteryselfchoiceClock = new util.Clock();
  pickacard_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pickacard_text',
    text: 'Please select whether you believe the card will be higher or lower than 5. Press [h] for higher or [l] for lower.',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.65], height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  higher_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'higher_text',
    text: 'Higher',
    font: 'Open Sans',
    units: undefined,
    pos: [0.3, (- 0.55)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0
  });

  lower_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'lower_text',
    text: 'Lower',
    font: 'Open Sans',
    units: undefined,
    pos: [(- 0.3), (- 0.55)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0
  });

  lotteryguess_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  responsefeedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'responsefeedback',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.7)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('cornflowerblue'),  opacity: undefined,
    depth: -6.0
  });

  block1_cardimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'block1_cardimage', units : undefined,
    image : 'Task_Images/facedown_card.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0
  });
  // Initialize components for Routine "Continue"
  ContinueClock = new util.Clock();
  resumeafterlottery_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  resumetext_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'resumetext_text',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.12,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0
  });

  mouseClock =  new util.Clock();
  userMouse = new core.Mouse({
    win: psychoJS.window,
    name: 'userMouse',
  });
  // Initialize components for Routine "SalienceRating"
  SalienceRatingClock = new util.Clock();
  // Run 'Begin Experiment' code from saliencyrating_code
  // salience_slider = new visual.Slider({"win": psychoJS.window, "name": "slider", "startValue": 999, "size": [1.0, 0.1], "pos": [0, (- 0.4)], "units": null, "labels": [1, 2, 3, 4, 5], "ticks": [1, 2, 3, 4, 5], "granularity": 0.0, "style": "rating", "styleTweaks": ["labels45", "triangleMarker"], "opacity": null, "labelColor": "white", "markerColor": "cornflowerblue", "lineColor": "white", "colorSpace": "rgb", "font": "Open Sans", "labelHeight": 0.05, "flip": false, "ori": 0.0, "depth": (- 5), "readOnly": false});
  salience_slider = new visual.Slider({
    win: psychoJS.window,
    name: "slider",
    size: [1.0, 0.1],
    pos: [0, -0.2], //[0, (- 0.4)]
    units: null,
    labels: [1, 2, 3, 4, 5],
    ticks: [1, 2, 3, 4, 5],
    granularity: 0.0,
    opacity: null,
    style: [visual.Slider.Style.RATING],
    labelColor: "white",
    markerColor: "cornflowerblue",
    lineColor: "white",
    colorSpace: "rgb",
    font: "Open Sans",
    labelHeight: 0.05,
    flip: false,
    ori: 0.0,
    depth: (- 5),
    readOnly: false,
    autoDraw: false});

  saliencequestion_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'saliencequestion_text',
    text: '',
    font: 'Open Sans',
    units: undefined,
    // (0,0.)
    pos: [0, 0.8], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  salienceavatar_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'salienceavatar_image', units : undefined,
    image : undefined, mask : undefined,
    ori : 0.0, //(0,0)
    pos : [0, 0.3],
    size : [0.35, 0.55], //[0.3, 0.55]
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0
  });
  saliencecontinue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'saliencecontinue_text',
    text: 'To continue, click the square when your desired rating appears',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.8)], //[0, (- 0.8)]
    height: 0.045, //0.07
     wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0
  });

  displayrating_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displayrating_text',
    text: 'Click line',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.6)], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('cornflowerblue'),  opacity: undefined,
    depth: -5.0
  });

  Salience_Button = new visual.Rect ({
   win: psychoJS.window, name: 'polygon',
   width: [0.25, 0.25][0], height: [0.25, 0.25][1],
   ori: 0, pos: [0, (- 0.6)],
   lineWidth: 1, lineColor: new util.Color('white'),
   fillColor: undefined,
   opacity: 1, depth: -1, interpolate: true,
 });

  // Initialize components for Routine "StressLevel"
  StressLevelClock = new util.Clock();
  // Run 'Begin Experiment' code from stresslevelslider
  // stress_slider = new visual.Slider({"win": psychoJS.window, "name": "slider", "startValue": 999, "size": [1.0, 0.1], "pos": [0, (- 0.4)], "units": null, "labels": [1, 2, 3, 4, 5, 6, 7, 8, 9], "ticks": [1, 2, 3, 4, 5, 6, 7, 8, 9], "granularity": 0.0, "style": "rating", "styleTweaks": ["labels45", "triangleMarker"], "opacity": null, "labelColor": "white", "markerColor": "cornflowerblue", "lineColor": "white", "colorSpace": "rgb", "font": "Open Sans", "labelHeight": 0.05, "flip": false, "ori": 0.0, "depth": (- 5), "readOnly": false});
  stress_slider = new visual.Slider({
    win: psychoJS.window,
    name: "slider",
    size: [1.0, 0.1],
    pos: [0, -0.2], //[0,(-0.4)]
    units: null,
    labels: ['1 (Bad)', '2', '3', '4', '5','6','7','8','9 (Good)'],
    ticks: [1, 2, 3, 4, 5,6,7,8,9],
    granularity: 0.0,
    opacity: null,
    style: [visual.Slider.Style.RATING],
    labelColor: "white",
    markerColor: "cornflowerblue",
    lineColor: "white",
    colorSpace: "rgb",
    font: "Open Sans",
    labelHeight: 0.05,
    flip: false,
    ori: 0.0,
    depth: (- 5),
    readOnly: false});

  Stress_Button = new visual.Rect ({
     win: psychoJS.window, name: 'polygon',
     width: [0.25, 0.25][0], height: [0.25, 0.25][1],
     ori: 0, pos: [0, (- 0.6)],
     lineWidth: 1, lineColor: new util.Color('white'),
     fillColor: undefined,
     opacity: 1, depth: -1, interpolate: true,
   });

  stresslevel_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stresslevel_text',
    text: '',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0.4], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0
  });

  stresslevel_keypress = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  displaystressrating_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'displaystressrating_text',
    text: 'Click line',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.6)], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('cornflowerblue'),  opacity: undefined,
    depth: -5.0
  });

  stresscontinue_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stresscontinue_text',
    text: 'To continue, click the square when your desired rating appears',
    font: 'Open Sans',
    units: undefined,
    pos: [0, (- 0.8)], //[0, (- 0.8)]
    height: 0.045, //0.07
     wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0
  });

end_screenclock = new util.Clock();
end_screen = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_screen',
    text: 'You have now reached the end of the task. \n\n\nPress space to be redirected to complete the post-task survey.\n',
    font: 'Open Sans',
    units: undefined,
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0
  });
  end_screen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  endwelcomescreen_keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});

  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _endwelcomescreen_keys_allKeys;
var Welcome_ScreenComponents;
function Welcome_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Welcome_Screen' ---
    t = 0;
    Welcome_ScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endwelcomescreen_keys.keys = undefined;
    endwelcomescreen_keys.rt = undefined;
    _endwelcomescreen_keys_allKeys = [];
    // keep track of which components have finished
    Welcome_ScreenComponents = [];
    Welcome_ScreenComponents.push(Welcome);
    Welcome_ScreenComponents.push(endwelcomescreen_keys);

    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Welcome_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome_Screen' ---
    // get current time
    t = Welcome_ScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *Welcome* updates
    if (t >= 0.0 && Welcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Welcome.tStart = t;  // (not accounting for frame time here)
      Welcome.frameNStart = frameN;  // exact frame index

      Welcome.setAutoDraw(true);
    }


    // *endwelcomescreen_keys* updates
    if (t >= 0.0 && endwelcomescreen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endwelcomescreen_keys.tStart = t;  // (not accounting for frame time here)
      endwelcomescreen_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endwelcomescreen_keys.clearEvents(); });
    }

    if (endwelcomescreen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endwelcomescreen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endwelcomescreen_keys_allKeys = _endwelcomescreen_keys_allKeys.concat(theseKeys);
      if (_endwelcomescreen_keys_allKeys.length > 0) {
        endwelcomescreen_keys.keys = _endwelcomescreen_keys_allKeys[_endwelcomescreen_keys_allKeys.length - 1].name;  // just the last key pressed
        endwelcomescreen_keys.rt = _endwelcomescreen_keys_allKeys[_endwelcomescreen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome_Screen' ---
    for (const thisComponent of Welcome_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endwelcomescreen_keys.corr, level);
    }
    //add particpiant ID to PROLIFIC_ID column
    psychoJS.experiment.addData('PROLIFIC_ID', expInfo['participant'])
    psychoJS.experiment.addData('endwelcomescreen_keys.keys', endwelcomescreen_keys.keys);
    if (typeof endwelcomescreen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endwelcomescreen_keys.rt', endwelcomescreen_keys.rt);
        routineTimer.reset();
        }

    endwelcomescreen_keys.stop();
    // the Routine "Welcome_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var testComponents;
function testRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'test' ---
    t = 0;
    testClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    testComponents = [];

    for (const thisComponent of testComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function testRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'test' ---
    // get current time
    t = testClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of testComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function testRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'test' ---
    for (const thisComponent of testComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _endinstructionscreen_keys_allKeys;
var First_InstructionsComponents;
function First_InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'First_Instructions' ---
    t = 0;
    First_InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    endinstructionscreen_keys.keys = undefined;
    endinstructionscreen_keys.rt = undefined;
    _endinstructionscreen_keys_allKeys = [];
    // keep track of which components have finished
    First_InstructionsComponents = [];
    First_InstructionsComponents.push(FirstInstructions);
    First_InstructionsComponents.push(endinstructionscreen_keys);

    for (const thisComponent of First_InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function First_InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'First_Instructions' ---
    // get current time
    t = First_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *FirstInstructions* updates
    if (t >= 0.0 && FirstInstructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FirstInstructions.tStart = t;  // (not accounting for frame time here)
      FirstInstructions.frameNStart = frameN;  // exact frame index

      FirstInstructions.setAutoDraw(true);
    }


    // *endinstructionscreen_keys* updates
    if (t >= 0.0 && endinstructionscreen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endinstructionscreen_keys.tStart = t;  // (not accounting for frame time here)
      endinstructionscreen_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endinstructionscreen_keys.clearEvents(); });
    }

    if (endinstructionscreen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endinstructionscreen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endinstructionscreen_keys_allKeys = _endinstructionscreen_keys_allKeys.concat(theseKeys);
      if (_endinstructionscreen_keys_allKeys.length > 0) {
        endinstructionscreen_keys.keys = _endinstructionscreen_keys_allKeys[_endinstructionscreen_keys_allKeys.length - 1].name;  // just the last key pressed
        endinstructionscreen_keys.rt = _endinstructionscreen_keys_allKeys[_endinstructionscreen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of First_InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function First_InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'First_Instructions' ---
    for (const thisComponent of First_InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endinstructionscreen_keys.corr, level);
    }
    psychoJS.experiment.addData('endinstructionscreen_keys.keys', endinstructionscreen_keys.keys);
    if (typeof endinstructionscreen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endinstructionscreen_keys.rt', endinstructionscreen_keys.rt);
        routineTimer.reset();
        }

    endinstructionscreen_keys.stop();
    // the Routine "First_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var entiretaskloop;
function entiretaskloopLoopBegin(entiretaskloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    entiretaskloop = new TrialHandler({
      psychoJS: psychoJS,
      //nReps: 5, method: TrialHandler.Method.SEQUENTIAL,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: `Participant_Images/${expInfo["participant"]}/${expInfo["participant"]}_trials.csv`,
      seed: undefined, name: 'entiretaskloop'
    });
    psychoJS.experiment.addLoop(entiretaskloop); // add the loop to the experiment
    currentLoop = entiretaskloop;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisEntiretaskloop of entiretaskloop) {
      snapshot = entiretaskloop.getSnapshot();
      entiretaskloopLoopScheduler.add(importConditions(snapshot));
      entiretaskloopLoopScheduler.add(partner_codeRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(partner_codeRoutineEachFrame());
      entiretaskloopLoopScheduler.add(partner_codeRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineEachFrame());
      entiretaskloopLoopScheduler.add(WaitingToMatchRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineEachFrame());
      entiretaskloopLoopScheduler.add(Partner_MatchRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineEachFrame());
      entiretaskloopLoopScheduler.add(Photo_ShareRoutineEnd(snapshot));
      // entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineBegin(snapshot));
      // entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineEachFrame());
      // entiretaskloopLoopScheduler.add(WaitingforfeedbackRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(feedbackRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(feedbackRoutineEachFrame());
      entiretaskloopLoopScheduler.add(feedbackRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(continuesharingRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(continuesharingRoutineEachFrame());
      entiretaskloopLoopScheduler.add(continuesharingRoutineEnd(snapshot));
      const lotteryloopLoopScheduler = new Scheduler(psychoJS);
      entiretaskloopLoopScheduler.add(lotteryloopLoopBegin(lotteryloopLoopScheduler, snapshot));
      entiretaskloopLoopScheduler.add(lotteryloopLoopScheduler);
      entiretaskloopLoopScheduler.add(lotteryloopLoopEnd);
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineEachFrame());
      entiretaskloopLoopScheduler.add(SalienceRatingRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(StressLevelRoutineBegin(snapshot));
      entiretaskloopLoopScheduler.add(StressLevelRoutineEachFrame());
      entiretaskloopLoopScheduler.add(StressLevelRoutineEnd(snapshot));
      entiretaskloopLoopScheduler.add(entiretaskloopLoopEndIteration(entiretaskloopLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


var lotteryloop;
function lotteryloopLoopBegin(lotteryloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    lotteryloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: startlottery, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'lotteryloop'
    });
    psychoJS.experiment.addLoop(lotteryloop); // add the loop to the experiment
    currentLoop = lotteryloop;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisLotteryloop of lotteryloop) {
      snapshot = lotteryloop.getSnapshot();
      lotteryloopLoopScheduler.add(importConditions(snapshot));
      lotteryloopLoopScheduler.add(ChoiceRoutineBegin(snapshot));
      lotteryloopLoopScheduler.add(ChoiceRoutineEachFrame());
      lotteryloopLoopScheduler.add(ChoiceRoutineEnd(snapshot));
      const computerchoiceLoopScheduler = new Scheduler(psychoJS);
      lotteryloopLoopScheduler.add(computerchoiceLoopBegin(computerchoiceLoopScheduler, snapshot));
      lotteryloopLoopScheduler.add(computerchoiceLoopScheduler);
      lotteryloopLoopScheduler.add(computerchoiceLoopEnd);
      const selfchoiceLoopScheduler = new Scheduler(psychoJS);
      lotteryloopLoopScheduler.add(selfchoiceLoopBegin(selfchoiceLoopScheduler, snapshot));
      lotteryloopLoopScheduler.add(selfchoiceLoopScheduler);
      lotteryloopLoopScheduler.add(selfchoiceLoopEnd);
      lotteryloopLoopScheduler.add(ContinueRoutineBegin(snapshot));
      lotteryloopLoopScheduler.add(ContinueRoutineEachFrame());
      lotteryloopLoopScheduler.add(ContinueRoutineEnd(snapshot));
      lotteryloopLoopScheduler.add(lotteryloopLoopEndIteration(lotteryloopLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


var computerchoice;
function computerchoiceLoopBegin(computerchoiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    computerchoice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: comprunOrNot, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'computerchoice'
    });
    psychoJS.experiment.addLoop(computerchoice); // add the loop to the experiment
    currentLoop = computerchoice;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisComputerchoice of computerchoice) {
      snapshot = computerchoice.getSnapshot();
      computerchoiceLoopScheduler.add(importConditions(snapshot));
      computerchoiceLoopScheduler.add(LotterycomputerchoiceRoutineBegin(snapshot));
      computerchoiceLoopScheduler.add(LotterycomputerchoiceRoutineEachFrame());
      computerchoiceLoopScheduler.add(LotterycomputerchoiceRoutineEnd(snapshot));
      computerchoiceLoopScheduler.add(computerchoiceLoopEndIteration(computerchoiceLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


async function computerchoiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(computerchoice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function computerchoiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var selfchoice;
function selfchoiceLoopBegin(selfchoiceLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop

    // set up handler to look after randomisation of conditions etc
    selfchoice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: selfrunOrNot, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'selfchoice'
    });
    psychoJS.experiment.addLoop(selfchoice); // add the loop to the experiment
    currentLoop = selfchoice;  // we're now the current loop

    // Schedule all the trials in the trialList:
    for (const thisSelfchoice of selfchoice) {
      snapshot = selfchoice.getSnapshot();
      selfchoiceLoopScheduler.add(importConditions(snapshot));
      selfchoiceLoopScheduler.add(LotteryselfchoiceRoutineBegin(snapshot));
      selfchoiceLoopScheduler.add(LotteryselfchoiceRoutineEachFrame());
      selfchoiceLoopScheduler.add(LotteryselfchoiceRoutineEnd(snapshot));
      selfchoiceLoopScheduler.add(selfchoiceLoopEndIteration(selfchoiceLoopScheduler, snapshot));
    }

    return Scheduler.Event.NEXT;
  }
}


async function selfchoiceLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(selfchoice);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function selfchoiceLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function lotteryloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(lotteryloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function lotteryloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function entiretaskloopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(entiretaskloop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function entiretaskloopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var partner_codeComponents;
function partner_codeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'partner_code' ---
    t = 0;
    partner_codeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    partner_codeComponents = [];

    for (const thisComponent of partner_codeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function partner_codeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'partner_code' ---
    // get current time
    t = partner_codeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of partner_codeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function partner_codeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'partner_code' ---
    for (const thisComponent of partner_codeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from partnermatchcode
    partnermatch = `You have matched with: ${Partner}`;
    if ((Partner === "Sam")) {
        partneravatar = "Task_Images/nerdemoji_nobackground.png";
    }
    if ((Partner === "Riley")) {
        partneravatar = "Task_Images/sunglassemoji_nobackground.png";
      }
    if ((Partner === "Alex")) {
        partneravatar = "Task_Images/cowboyemoji.png";
      }
    if ((Partner === "Taylor")) {
        partneravatar = "Task_Images/huggingemoji.png";

    } else {
        if ((Partner === "Charlie")) {
            partneravatar = "Task_Images/smilingemoji.png";
        }
      }

    // the Routine "partner_code" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var WaitingToMatchComponents;
function WaitingToMatchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'WaitingToMatch' ---
    t = 0;
    WaitingToMatchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(9.250000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showloadingbar
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6(TrialNumber, [1, 31, 61, 91, 121]))) {
        continueRoutine = false;
    }

    // keep track of which components have finished
    WaitingToMatchComponents = [];
    WaitingToMatchComponents.push(Match_text);
    WaitingToMatchComponents.push(syncing_text);
    WaitingToMatchComponents.push(text_0);
    WaitingToMatchComponents.push(Transparent);
    WaitingToMatchComponents.push(Loading_25);
    WaitingToMatchComponents.push(text_25);
    WaitingToMatchComponents.push(Loading_50);
    WaitingToMatchComponents.push(text_50);
    WaitingToMatchComponents.push(Loading_75);
    WaitingToMatchComponents.push(text_75);
    WaitingToMatchComponents.push(Loading_100);
    WaitingToMatchComponents.push(text_100);

    for (const thisComponent of WaitingToMatchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function WaitingToMatchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WaitingToMatch' ---
    // get current time
    t = WaitingToMatchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *Match_text* updates
    if (t >= 0.0 && Match_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Match_text.tStart = t;  // (not accounting for frame time here)
      Match_text.frameNStart = frameN;  // exact frame index

      Match_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Match_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Match_text.setAutoDraw(false);
    }

    // *syncing_text* updates
    if (t >= 3 && syncing_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      syncing_text.tStart = t;  // (not accounting for frame time here)
      syncing_text.frameNStart = frameN;  // exact frame index

      syncing_text.setAutoDraw(true);
    }

    frameRemains = 3 + 6.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (syncing_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      syncing_text.setAutoDraw(false);
    }

    // *text_0* updates
    if (t >= 3 && text_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_0.tStart = t;  // (not accounting for frame time here)
      text_0.frameNStart = frameN;  // exact frame index

      text_0.setAutoDraw(true);
    }

    frameRemains = 3 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_0.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_0.setAutoDraw(false);
    }

    // *Transparent* updates
    if (t >= 3 && Transparent.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Transparent.tStart = t;  // (not accounting for frame time here)
      Transparent.frameNStart = frameN;  // exact frame index

      Transparent.setAutoDraw(true);
    }

    frameRemains = 3 + 6.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Transparent.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Transparent.setAutoDraw(false);
    }

    // *Loading_25* updates
    if (t >= 4.25 && Loading_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_25.tStart = t;  // (not accounting for frame time here)
      Loading_25.frameNStart = frameN;  // exact frame index

      Loading_25.setAutoDraw(true);
    }

    frameRemains = 4.25 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_25.setAutoDraw(false);
    }

    // *text_25* updates
    if (t >= 4.25 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index

      text_25.setAutoDraw(true);
    }

    frameRemains = 4.25 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_25.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_25.setAutoDraw(false);
    }

    // *Loading_50* updates
    if (t >= 5.5 && Loading_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_50.tStart = t;  // (not accounting for frame time here)
      Loading_50.frameNStart = frameN;  // exact frame index

      Loading_50.setAutoDraw(true);
    }

    frameRemains = 5.5 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_50.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_50.setAutoDraw(false);
    }

    // *text_50* updates
    if (t >= 5.5 && text_50.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_50.tStart = t;  // (not accounting for frame time here)
      text_50.frameNStart = frameN;  // exact frame index

      text_50.setAutoDraw(true);
    }

    frameRemains = 5.5 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_50.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_50.setAutoDraw(false);
    }

    // *Loading_75* updates
    if (t >= 6.75 && Loading_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_75.tStart = t;  // (not accounting for frame time here)
      Loading_75.frameNStart = frameN;  // exact frame index

      Loading_75.setAutoDraw(true);
    }

    frameRemains = 6.75 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_75.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_75.setAutoDraw(false);
    }

    // *text_75* updates
    if (t >= 6.75 && text_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_75.tStart = t;  // (not accounting for frame time here)
      text_75.frameNStart = frameN;  // exact frame index

      text_75.setAutoDraw(true);
    }

    frameRemains = 6.75 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_75.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_75.setAutoDraw(false);
    }

    // *Loading_100* updates
    if (t >= 8 && Loading_100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Loading_100.tStart = t;  // (not accounting for frame time here)
      Loading_100.frameNStart = frameN;  // exact frame index

      Loading_100.setAutoDraw(true);
    }

    frameRemains = 8 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Loading_100.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Loading_100.setAutoDraw(false);
    }

    // *text_100* updates
    if (t >= 8 && text_100.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_100.tStart = t;  // (not accounting for frame time here)
      text_100.frameNStart = frameN;  // exact frame index

      text_100.setAutoDraw(true);
    }

    frameRemains = 8 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_100.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_100.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WaitingToMatchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WaitingToMatchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WaitingToMatch' ---
    for (const thisComponent of WaitingToMatchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _endpartnermatch_keys_allKeys;
var Partner_MatchComponents;
function Partner_MatchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Partner_Match' ---
    t = 0;
    Partner_MatchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from showpartnermatch
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6(TrialNumber, [1, 31, 61, 91, 121]))) {
        continueRoutine = false;
    }

    Youhavematched.setText(partnermatch);
    partneremoji_image.setImage(partneravatar);
    endpartnermatch_keys.keys = undefined;
    endpartnermatch_keys.rt = undefined;
    _endpartnermatch_keys_allKeys = [];
    // keep track of which components have finished
    Partner_MatchComponents = [];
    Partner_MatchComponents.push(Youhavematched);
    Partner_MatchComponents.push(partneremoji_image);
    Partner_MatchComponents.push(endpartnermatch_keys);
    Partner_MatchComponents.push(PressToContinue);

    for (const thisComponent of Partner_MatchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Partner_MatchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Partner_Match' ---
    // get current time
    t = Partner_MatchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *Youhavematched* updates
    if (t >= 0.0 && Youhavematched.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Youhavematched.tStart = t;  // (not accounting for frame time here)
      Youhavematched.frameNStart = frameN;  // exact frame index

      Youhavematched.setAutoDraw(true);
    }


    // *partneremoji_image* updates
    if (t >= 0.0 && partneremoji_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      partneremoji_image.tStart = t;  // (not accounting for frame time here)
      partneremoji_image.frameNStart = frameN;  // exact frame index

      partneremoji_image.setAutoDraw(true);
    }


    // *endpartnermatch_keys* updates
    if (t >= 0.0 && endpartnermatch_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endpartnermatch_keys.tStart = t;  // (not accounting for frame time here)
      endpartnermatch_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endpartnermatch_keys.clearEvents(); });
    }

    if (endpartnermatch_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = endpartnermatch_keys.getKeys({keyList: ['space'], waitRelease: false});
      _endpartnermatch_keys_allKeys = _endpartnermatch_keys_allKeys.concat(theseKeys);
      if (_endpartnermatch_keys_allKeys.length > 0) {
        endpartnermatch_keys.keys = _endpartnermatch_keys_allKeys[_endpartnermatch_keys_allKeys.length - 1].name;  // just the last key pressed
        endpartnermatch_keys.rt = _endpartnermatch_keys_allKeys[_endpartnermatch_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *PressToContinue* updates
    if (t >= 0.0 && PressToContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PressToContinue.tStart = t;  // (not accounting for frame time here)
      PressToContinue.frameNStart = frameN;  // exact frame index

      PressToContinue.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Partner_MatchComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Partner_MatchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Partner_Match' ---
    for (const thisComponent of Partner_MatchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(endpartnermatch_keys.corr, level);
    }
    psychoJS.experiment.addData('endpartnermatch_keys.keys', endpartnermatch_keys.keys);
    if (typeof endpartnermatch_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endpartnermatch_keys.rt', endpartnermatch_keys.rt);
        routineTimer.reset();
        }

    endpartnermatch_keys.stop();
    // the Routine "Partner_Match" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var Photo_ShareComponents;
function Photo_ShareRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Photo_Share' ---
    t = 0;
    Photo_ShareClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    //routineTimer.add(3.000000);
    routineTimer.add(FeedbackWait);

    // update component parameters for each repeat
    participantimage_image.setImage(Photos);
    // keep track of which components have finished
    Photo_ShareComponents = [];
    Photo_ShareComponents.push(photobeingshared_text);
    Photo_ShareComponents.push(waitforfeedback_text);
    Photo_ShareComponents.push(participantimage_image);

    for (const thisComponent of Photo_ShareComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Photo_ShareRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Photo_Share' ---
    // get current time
    //routineTimer.reset(Waiting);

    t = Photo_ShareClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *photobeingshared_text* updates
    if (t >= 0.0 && photobeingshared_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      photobeingshared_text.tStart = t;  // (not accounting for frame time here)
      photobeingshared_text.frameNStart = frameN;  // exact frame index

      photobeingshared_text.setAutoDraw(true);
    }

  //  frameRemains = 0.0 + parseFloat(Waiting) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    frameRemains = 0.0 + FeedbackWait - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (photobeingshared_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      photobeingshared_text.setAutoDraw(false);
    }

    // *waitforfeedback_text* updates
    if (t >= 0.0 && waitforfeedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      waitforfeedback_text.tStart = t;  // (not accounting for frame time here)
      waitforfeedback_text.frameNStart = frameN;  // exact frame index

      waitforfeedback_text.setAutoDraw(true);
    }

  //  frameRemains = 0.0 + parseFloat(Waiting) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    frameRemains = 0.0 + FeedbackWait - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (waitforfeedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      waitforfeedback_text.setAutoDraw(false);
    }

    // *participantimage_image* updates
    if (t >= 0.0 && participantimage_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      participantimage_image.tStart = t;  // (not accounting for frame time here)
      participantimage_image.frameNStart = frameN;  // exact frame index

      participantimage_image.setAutoDraw(true);
    }

    //frameRemains = 0.0 + parseFloat(Waiting) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    frameRemains = 0.0 + FeedbackWait - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (participantimage_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      participantimage_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Photo_ShareComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Photo_ShareRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Photo_Share' ---
    for (const thisComponent of Photo_ShareComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from initiatefeedbackresponses
    feedbackresponses = `${Partner} ${Feedback} your photo`;
    if ((Feedback === "liked")) {
        fdbkimage = "Task_Images/thumbsup.png";
    } else {
        if ((Feedback === "did not like")) {
            fdbkimage = "Task_Images/thumbsdown.png";
        }
    }

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    displayfeedback_text.setText(feedbackresponses);
    fdbkimage_image.setImage(fdbkimage);
    // Run 'Begin Routine' code from initiatelottery_code
    if (((TrialNumber % 5) === 0)) {
        startlottery = 1;
    } else {
        startlottery = 0;
    }

    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(displayfeedback_text);
    feedbackComponents.push(fdbkimage_image);

    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *displayfeedback_text* updates
    if (t >= 0.0 && displayfeedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      displayfeedback_text.tStart = t;  // (not accounting for frame time here)
      displayfeedback_text.frameNStart = frameN;  // exact frame index

      displayfeedback_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (displayfeedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      displayfeedback_text.setAutoDraw(false);
    }

    // *fdbkimage_image* updates
    if (t >= 0.0 && fdbkimage_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fdbkimage_image.tStart = t;  // (not accounting for frame time here)
      fdbkimage_image.frameNStart = frameN;  // exact frame index

      fdbkimage_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fdbkimage_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fdbkimage_image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    for (const thisComponent of feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _sharenextphoto_key_allKeys;
var continuesharingComponents;
function continuesharingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'continuesharing' ---
    t = 0;
    continuesharingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    sharenextphoto_key.keys = undefined;
    sharenextphoto_key.rt = undefined;
    _sharenextphoto_key_allKeys = [];
    // Run 'Begin Routine' code from hidecontinuesharingroutine_code
    if ((startlottery === 1)) {
        continueRoutine = false;
    } else {
        continueRoutine = true;
    }

    // keep track of which components have finished
    continuesharingComponents = [];
    continuesharingComponents.push(presstosharenextphoto_text);
    continuesharingComponents.push(sharenextphoto_key);

    for (const thisComponent of continuesharingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function continuesharingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'continuesharing' ---
    // get current time
    t = continuesharingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *presstosharenextphoto_text* updates
    if (t >= 0.0 && presstosharenextphoto_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      presstosharenextphoto_text.tStart = t;  // (not accounting for frame time here)
      presstosharenextphoto_text.frameNStart = frameN;  // exact frame index

      presstosharenextphoto_text.setAutoDraw(true);
    }


    // *sharenextphoto_key* updates
    if (t >= 0.0 && sharenextphoto_key.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sharenextphoto_key.tStart = t;  // (not accounting for frame time here)
      sharenextphoto_key.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { sharenextphoto_key.clearEvents(); });
    }

    if (sharenextphoto_key.status === PsychoJS.Status.STARTED) {
      let theseKeys = sharenextphoto_key.getKeys({keyList: ['space'], waitRelease: false});
      _sharenextphoto_key_allKeys = _sharenextphoto_key_allKeys.concat(theseKeys);
      if (_sharenextphoto_key_allKeys.length > 0) {
        sharenextphoto_key.keys = _sharenextphoto_key_allKeys[0].name;  // just the first key pressed
        sharenextphoto_key.rt = _sharenextphoto_key_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of continuesharingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function continuesharingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'continuesharing' ---
    for (const thisComponent of continuesharingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(sharenextphoto_key.corr, level);
    }
    psychoJS.experiment.addData('sharenextphoto_key.keys', sharenextphoto_key.keys);
    if (typeof sharenextphoto_key.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('sharenextphoto_key.rt', sharenextphoto_key.rt);
        routineTimer.reset();
        }

    sharenextphoto_key.stop();
    // the Routine "continuesharing" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _choice_keys_allKeys;
var ChoiceComponents;
function ChoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Choice' ---
    t = 0;
    conditionalBlank.setText('');
    ChoiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    choice_keys.keys = undefined;
    choice_keys.rt = undefined;
    _choice_keys_allKeys = [];
    // keep track of which components have finished
    ChoiceComponents = [];
    ChoiceComponents.push(lotterychoice_text);
    ChoiceComponents.push(computer_text);
    ChoiceComponents.push(self_text);
    ChoiceComponents.push(conditionalBlank);
    ChoiceComponents.push(choice_keys);

    for (const thisComponent of ChoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var random_entry;
var DecisionColor;
function ChoiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Choice' ---
    // get current time
    t = ChoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *lotterychoice_text* updates
    if (t >= 0.0 && lotterychoice_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lotterychoice_text.tStart = t;  // (not accounting for frame time here)
      lotterychoice_text.frameNStart = frameN;  // exact frame index

      lotterychoice_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lotterychoice_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lotterychoice_text.setAutoDraw(false);
    }

    // *computer_text* updates
    if (t >= 0.0 && computer_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      computer_text.tStart = t;  // (not accounting for frame time here)
      computer_text.frameNStart = frameN;  // exact frame index

      computer_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (computer_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      computer_text.setAutoDraw(false);
    }

    // *self_text* updates
    if (t >= 0.0 && self_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_text.tStart = t;  // (not accounting for frame time here)
      self_text.frameNStart = frameN;  // exact frame index

      self_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (self_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      self_text.setAutoDraw(false);
    }
    // Run 'Each Frame' code from setvariables_code
    var random_item;
    random_item = Math.floor(Math.random() * computer_choice.length);
    random_entry = computer_choice[random_item]




    // *choice_keys* updates
    if (t >= 0.0 && choice_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice_keys.tStart = t;  // (not accounting for frame time here)
      choice_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choice_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choice_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choice_keys.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (choice_keys.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      choice_keys.status = PsychoJS.Status.FINISHED;
  }

    if (choice_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice_keys.getKeys({keyList: ['c', 's'], waitRelease: false});
      _choice_keys_allKeys = _choice_keys_allKeys.concat(theseKeys);
      if (_choice_keys_allKeys.length > 0) {
        choice_keys.keys = _choice_keys_allKeys[_choice_keys_allKeys.length - 1].name;  // just the last key pressed
        choice_keys.rt = _choice_keys_allKeys[_choice_keys_allKeys.length - 1].rt;
      }
    }
    DecisionColor = "cornflowerblue";
    if ((choice_keys.keys === "c")) {
        computer_text.setColor(new util.Color(DecisionColor));



    } else {
        if ((choice_keys.keys === "s")) {
            self_text.setColor(new util.Color(DecisionColor));
      }

      // *conditionalBlank* updates
      if (choice_keys.keys > 0 && conditionalBlank.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        conditionalBlank.tStart = t;  // (not accounting for frame time here)
        conditionalBlank.frameNStart = frameN;  // exact frame index
        conditionalBlank.setAutoDraw(true);
      }

      if (conditionalBlank.status === PsychoJS.Status.STARTED && t >= (conditionalBlank.tStart + 2.0)) {
      conditionalBlank.setAutoDraw(false);
      }

    //   show the response for 2 seconds, then move on to next trial
      if (conditionalBlank.status == PsychoJS.Status.FINISHED){
         self_text.setAutoDraw(false);
         computer_text.setAutoDraw(false);
         lotterychoice_text.setAutoDraw(false);

         continueRoutine = false;
       }

    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ChoiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ChoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Choice' ---
    for (const thisComponent of ChoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }



    // Run 'End Routine' code from setvariables_code
    if ((choice_keys.keys === "c")) {
        selfrunOrNot = 0;
        comprunOrNot = 1;
        playlottery = 0;
        computer_text.setColor(new util.Color("white"));
    } else {
        if ((choice_keys.keys === "s")) {
            selfrunOrNot = 1;
            comprunOrNot = 0;
            playlottery = 1;
            self_text.setColor(new util.Color("white"));
        } else {
            selfrunOrNot = 0;
            comprunOrNot = 0;
            playlottery = 999;
        }
    }

    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(choice_keys.corr, level);
    }
    psychoJS.experiment.addData('choice_keys.keys', choice_keys.keys);
    psychoJS.experiment.addData('playlottery', playlottery);
    if (typeof choice_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice_keys.rt', choice_keys.rt);
        }

    choice_keys.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var LotterycomputerchoiceComponents;
function LotterycomputerchoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Lotterycomputerchoice' ---
    t = 0;
    LotterycomputerchoiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from skipcomputerchoice_code
    response_msg = `The computer has chosen ${random_entry}.`;

    computerresponse.setText(response_msg);
    // keep track of which components have finished
    LotterycomputerchoiceComponents = [];
    LotterycomputerchoiceComponents.push(lotterycard);
    LotterycomputerchoiceComponents.push(Block1_facedowncard);
    LotterycomputerchoiceComponents.push(computerresponse);

    for (const thisComponent of LotterycomputerchoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function LotterycomputerchoiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Lotterycomputerchoice' ---
    // get current time
    t = LotterycomputerchoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *lotterycard* updates
    if (t >= 0.0 && lotterycard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lotterycard.tStart = t;  // (not accounting for frame time here)
      lotterycard.frameNStart = frameN;  // exact frame index

      lotterycard.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lotterycard.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lotterycard.setAutoDraw(false);
    }

    // *Block1_facedowncard* updates
    if (t >= 0.0 && Block1_facedowncard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Block1_facedowncard.tStart = t;  // (not accounting for frame time here)
      Block1_facedowncard.frameNStart = frameN;  // exact frame index

      Block1_facedowncard.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Block1_facedowncard.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Block1_facedowncard.setAutoDraw(false);
    }

    // *computerresponse* updates
    if (t >= 1 && computerresponse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      computerresponse.tStart = t;  // (not accounting for frame time here)
      computerresponse.frameNStart = frameN;  // exact frame index

      computerresponse.setAutoDraw(true);
    }

    frameRemains = 2 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (computerresponse.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      computerresponse.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LotterycomputerchoiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LotterycomputerchoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Lotterycomputerchoice' ---
    for (const thisComponent of LotterycomputerchoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _lotteryguess_keys_allKeys;
var LotteryselfchoiceComponents;
function LotteryselfchoiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Lotteryselfchoice' ---
    t = 0;
    LotteryselfchoiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(8.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from skipselfchoice_code_2
    /* Syntax Error: Fix Python code */
    lotteryguess_keys.keys = undefined;
    lotteryguess_keys.rt = undefined;
    _lotteryguess_keys_allKeys = [];
    responsefeedback.setText(feedback_msg);
    // keep track of which components have finished
    LotteryselfchoiceComponents = [];
    LotteryselfchoiceComponents.push(pickacard_text);
    LotteryselfchoiceComponents.push(higher_text);
    LotteryselfchoiceComponents.push(lower_text);
    LotteryselfchoiceComponents.push(lotteryguess_keys);
    LotteryselfchoiceComponents.push(responsefeedback);
    LotteryselfchoiceComponents.push(block1_cardimage);

    for (const thisComponent of LotteryselfchoiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

var DecisionColor;
function LotteryselfchoiceRoutineEachFrame() {
  return async function () {
    DecisionColor = "cornflowerblue";
    //--- Loop for each frame of Routine 'Lotteryselfchoice' ---
    // get current time
    t = LotteryselfchoiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *pickacard_text* updates
    if (t >= 0.0 && pickacard_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pickacard_text.tStart = t;  // (not accounting for frame time here)
      pickacard_text.frameNStart = frameN;  // exact frame index

      pickacard_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pickacard_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pickacard_text.setAutoDraw(false);
    }

    // *higher_text* updates
    if (t >= 0.0 && higher_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      higher_text.tStart = t;  // (not accounting for frame time here)
      higher_text.frameNStart = frameN;  // exact frame index

      higher_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (higher_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      higher_text.setAutoDraw(false);
    }

    // *lower_text* updates
    if (t >= 0.0 && lower_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lower_text.tStart = t;  // (not accounting for frame time here)
      lower_text.frameNStart = frameN;  // exact frame index

      lower_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lower_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lower_text.setAutoDraw(false);
    }

    // *lotteryguess_keys* updates
    if (t >= 0 && lotteryguess_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      lotteryguess_keys.tStart = t;  // (not accounting for frame time here)
      lotteryguess_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { lotteryguess_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { lotteryguess_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { lotteryguess_keys.clearEvents(); });
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (lotteryguess_keys.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      lotteryguess_keys.status = PsychoJS.Status.FINISHED;
  }

    if (lotteryguess_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = lotteryguess_keys.getKeys({keyList: ['h', 'l'], waitRelease: false});
      _lotteryguess_keys_allKeys = _lotteryguess_keys_allKeys.concat(theseKeys);
      if (_lotteryguess_keys_allKeys.length > 0) {
        lotteryguess_keys.keys = _lotteryguess_keys_allKeys[0].name;  // just the first key pressed
        lotteryguess_keys.rt = _lotteryguess_keys_allKeys[0].rt;
      }
    }

    // Run 'Each Frame' code from displaylotterychoice_code
    if ((lotteryguess_keys.keys === "l")) {
        feedback_msg = `You have chosen lower.`;
        lower_text.setColor(new util.Color(DecisionColor));
    } else {
        if ((lotteryguess_keys.keys === "h")) {
            feedback_msg = `You have chosen higher.`;
            higher_text.setColor(new util.Color(DecisionColor));
        } else {
            feedback_msg = `No response recorded.`;
        }
    }
    responsefeedback.setText(feedback_msg);


    // *responsefeedback* updates
    if (t >= 4 && responsefeedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responsefeedback.tStart = t;  // (not accounting for frame time here)
      responsefeedback.frameNStart = frameN;  // exact frame index

      responsefeedback.setAutoDraw(true);
    }

    frameRemains = 4 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (responsefeedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      responsefeedback.setAutoDraw(false);
    }

    // *block1_cardimage* updates
    if (t >= 0.0 && block1_cardimage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      block1_cardimage.tStart = t;  // (not accounting for frame time here)
      block1_cardimage.frameNStart = frameN;  // exact frame index

      block1_cardimage.setAutoDraw(true);
    }

    frameRemains = 0.0 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (block1_cardimage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      block1_cardimage.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LotteryselfchoiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LotteryselfchoiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Lotteryselfchoice' ---
    for (const thisComponent of LotteryselfchoiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(lotteryguess_keys.corr, level);
    }
    psychoJS.experiment.addData('lotteryguess_keys.keys', lotteryguess_keys.keys);
    if (typeof lotteryguess_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('lotteryguess_keys.rt', lotteryguess_keys.rt);
        }

    computer_text.setColor(new util.Color("white"));
    self_text.setColor(new util.Color("white"));
    higher_text.setColor(new util.Color("white"));
    lower_text.setColor(new util.Color("white"));
    lotteryguess_keys.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resumeafterlottery_keys_allKeys;
var ContinueComponents;
function ContinueRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'Continue' ---
    t = 0;
    ContinueClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    // if (((TrialNumber % 30) === 0)) {
    //     continueRoutine = false
    // }
    if (((comprunOrNot === 0) && (selfrunOrNot === 0))) {
        resumetext = "You missed an opportunity to play the lottery. \n\n\n Please be sure to respond faster on your next opportunity. \n\nPress space to continue.";
    } else {
        resumetext = "Press space to continue.";
    }

    resumeafterlottery_keys.keys = undefined;
    resumeafterlottery_keys.rt = undefined;
    _resumeafterlottery_keys_allKeys = [];
    resumetext_text.setText(resumetext);
    // keep track of which components have finished
    ContinueComponents = [];
    ContinueComponents.push(resumeafterlottery_keys);
    ContinueComponents.push(resumetext_text);

    for (const thisComponent of ContinueComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ContinueRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Continue' ---
    // get current time
    t = ContinueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *resumeafterlottery_keys* updates
    if (t >= 0.0 && resumeafterlottery_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resumeafterlottery_keys.tStart = t;  // (not accounting for frame time here)
      resumeafterlottery_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resumeafterlottery_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resumeafterlottery_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resumeafterlottery_keys.clearEvents(); });
    }

    if (resumeafterlottery_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = resumeafterlottery_keys.getKeys({keyList: ['space'], waitRelease: false});
      _resumeafterlottery_keys_allKeys = _resumeafterlottery_keys_allKeys.concat(theseKeys);
      if (_resumeafterlottery_keys_allKeys.length > 0) {
        resumeafterlottery_keys.keys = _resumeafterlottery_keys_allKeys[0].name;  // just the first key pressed
        resumeafterlottery_keys.rt = _resumeafterlottery_keys_allKeys[0].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }


    // *resumetext_text* updates
    if (t >= 0.0 && resumetext_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resumetext_text.tStart = t;  // (not accounting for frame time here)
      resumetext_text.frameNStart = frameN;  // exact frame index

      resumetext_text.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ContinueComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ContinueRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Continue' ---
    for (const thisComponent of ContinueComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resumeafterlottery_keys.corr, level);
    }
    psychoJS.experiment.addData('resumeafterlottery_keys.keys', resumeafterlottery_keys.keys);
    if (typeof resumeafterlottery_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resumeafterlottery_keys.rt', resumeafterlottery_keys.rt);
        routineTimer.reset();
        }

    resumeafterlottery_keys.stop();
    // the Routine "Continue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

// insert stress slider here 
var salienceratingtext;
var _key_resp_allKeys;
var SalienceRatingComponents;
var continueRoutine;
var salience_slider;
var SalienceRatingClock;
var mouserec;
var prevButtonState;
function SalienceRatingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'SalienceRating' ---
    t = 0;
    SalienceRatingClock.reset(); // clock
    frameN = -1;

    const trials = [30,60,90,120,150]

    if (trials.includes(TrialNumber) == true) {
      continueRoutine = true;

    } else {
      continueRoutine = false;
    }
    salienceratingtext = `You have finished sharing your photos with ${Partner}. \n\n How likely are you to share photos with ${Partner} in the future?
    Click the line to begin rating.`
    ;
    psychoJS.eventManager.clearEvents("keyboard");
    //salience_slider.markerPos = 3;

    saliencequestion_text.setText(salienceratingtext);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    salienceavatar_image.setImage(partneravatar);
    userMouse.clickReset();
    mouseClock.reset()
    mouserec = userMouse.getPos();
    userMouse.x = [];
    userMouse.y = [];
    userMouse.leftButton = [];
    userMouse.midButton = [];
    userMouse.rightButton = [];
    userMouse.time=[];
    prevButtonState = userMouse.getPressed();
    salience_slider.reset();
    displayrating_text.setText('Click line');
    // displayrating_text.setText(rating_forsalience); //get rid of NAN
    // keep track of which components have finished
    SalienceRatingComponents = [];
    SalienceRatingComponents.push(saliencequestion_text);
    SalienceRatingComponents.push(key_resp);
    SalienceRatingComponents.push(userMouse);
    SalienceRatingComponents.push(salienceavatar_image);
    SalienceRatingComponents.push(saliencecontinue_text);
    SalienceRatingComponents.push(displayrating_text);
    SalienceRatingComponents.push(salience_slider);
    SalienceRatingComponents.push(SalienceRatingClock);
    SalienceRatingComponents.push(Salience_Button);

    for (const thisComponent of SalienceRatingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var keys;
var rating_forsalience;
var salience_ratingvalue;
var gotValidClick;
var marker_pos;
var ratingvalue;
var buttonpress;
var finalmouseRT;
function SalienceRatingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SalienceRating' ---
    // get current time
    t = SalienceRatingClock.getTime();
    frameN = frameN + 1;
    let buttonpress = userMouse.getPressed(); // read mouse state
      const xys = userMouse.getPos();
      userMouse.x.push(xys[0]); // add mouse coordinates to x/y list, in principle for data storage, but not implemented right now
      userMouse.y.push(xys[1]);
      userMouse.leftButton.push(buttonpress[0]); // store buttons in button list, likewise for storage
      userMouse.midButton.push(buttonpress[1]);
      userMouse.rightButton.push(buttonpress[2]);


    // *saliencequestion_text* updates
    if (t >= 0.0 && saliencequestion_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      saliencequestion_text.tStart = t;  // (not accounting for frame time here)
      saliencequestion_text.frameNStart = frameN;  // exact frame index

      saliencequestion_text.setAutoDraw(true);
    }


    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }


    // *saliencecontinue_text* updates
  //  if (t >= 0.0 && saliencecontinue_text.status === PsychoJS.Status.NOT_STARTED) {
    if (key_resp.status === PsychoJS.Status.STARTED && saliencecontinue_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      saliencecontinue_text.tStart = t;  // (not accounting for frame time here)
      saliencecontinue_text.frameNStart = frameN;  // exact frame index

      saliencecontinue_text.setAutoDraw(true);
      Salience_Button.setAutoDraw(true);
      displayrating_text.setText('Click line');
      displayrating_text.setAutoDraw(true);
    }

    // *salienceavatar_image* updates
    if (t >= 0.0 && salienceavatar_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      salienceavatar_image.tStart = t;  // (not accounting for frame time here)
      salienceavatar_image.frameNStart = frameN;  // exact frame index

      salienceavatar_image.setAutoDraw(true);
    }





    // // *salience_slider* updates
    if (t >= 0.0 && salience_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      salience_slider.tStart = t;  // (not accounting for frame time here)
      salience_slider.frameNStart = frameN;  // exact frame index

      salience_slider.setAutoDraw(true);
    }

    var _pj;
      function _pj_snippets(container) {
          function in_es6(left, right) {
              if (((right instanceof Array) || ((typeof right) === "string"))) {
                  return (right.indexOf(left) > (- 1));
              } else {
                  if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                      return right.has(left);
                  } else {
                      return (left in right);
                  }
              }
          }
          container["in_es6"] = in_es6;
          return container;
      }
      _pj = {};
      _pj_snippets(_pj);

      const validclicks = [1,2,3,4,5]
        ratingvalue = salience_slider.getMarkerPos();
          if (1 < ratingvalue && ratingvalue < 1.5) {
                salience_slider.setMarkerPos(1)
                salience_slider.setRating(1)
                displayrating_text.setText(1);
                displayrating_text.setAutoDraw(true);

          }

          else if (1.5 < ratingvalue && ratingvalue < 2.5) {
                salience_slider.setMarkerPos(2)
                salience_slider.setRating(2)
                displayrating_text.setText(2);
                displayrating_text.setAutoDraw(true);

          }
            else if (2.5 < ratingvalue && ratingvalue < 3.5) {
                salience_slider.setMarkerPos(3)
                salience_slider.setRating(3)
                displayrating_text.setText(3);
                displayrating_text.setAutoDraw(true);

          }
          else if (3.5 < ratingvalue && ratingvalue < 4.5) {
              salience_slider.setMarkerPos(4)
              salience_slider.setRating(4)
              displayrating_text.setText(4);
              displayrating_text.setAutoDraw(true);
            }
          else if (4.5 < ratingvalue && ratingvalue < 5) {
              salience_slider.setMarkerPos(5)
              salience_slider.setRating(5)
              displayrating_text.setText(5);
              displayrating_text.setAutoDraw(true);

        }
            finalmouseRT = mouseClock.getTime(); // get mouse time, again for storage that is not implemented
            if (!buttonpress.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
              prevButtonState = buttonpress; //button state as of last frame, makes sure holding mouse down has not affected anything
              //debug code
              //console.log('new button state detected');
              if (buttonpress.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
                // check if the mouse was inside our 'clickable' objects
                gotValidClick = false;
                if (Salience_Button.contains(userMouse) && ratingvalue > 0) {
                  {gotValidClick = true};
                }
                if (gotValidClick === true) { // abort routine on response
                    continueRoutine = false;
                }
              }
            }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SalienceRatingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SalienceRatingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SalienceRating' ---
    for (const thisComponent of SalienceRatingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    function financial(x) {
                  return Number.parseFloat(x).toFixed(2);
                }


    entiretaskloop.addData("salience_rating", Math.round(salience_slider.getMarkerPos()*10/10));
    //entiretaskloop.addData("salience_rating", financial(salience_slider.getRating()))
    // update the trial handler);
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }

    key_resp.stop();
    // the Routine "SalienceRating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stressleveltext;
var _stresslevel_keypress_allKeys;
var StressLevelComponents;
var stress_slider;
var continueRoutine;
var StressLevelClock;
var mouserec;
var prevButtonState;
function StressLevelRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'StressLevel' ---
    t = 0;
    StressLevelClock.reset(); // clock
    frameN = -1;
    //continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from stresslevelslider
    const trials = [30,60,90,120,150]

    if (trials.includes(TrialNumber) == true) {
      continueRoutine = true;

    } else {
      continueRoutine = false;
    }
    stressleveltext = `How are you feeling right now?

    Click the line to begin rating.`
    ;
    psychoJS.eventManager.clearEvents("keyboard");
    // stress_slider.markerPos = 5;

    stresslevel_text.setText(stressleveltext);
    stresslevel_keypress.keys = undefined;
    stresslevel_keypress.rt = undefined;
    _stresslevel_keypress_allKeys = [];
    userMouse.clickReset();
    mouseClock.reset()
    mouserec = userMouse.getPos();
    userMouse.x = [];
    userMouse.y = [];
    userMouse.leftButton = [];
    userMouse.midButton = [];
    userMouse.rightButton = [];
    userMouse.time=[];
    prevButtonState = userMouse.getPressed();
    stress_slider.reset();
    displaystressrating_text.setText('Click line');
  //  displaystressrating_text.setText(rating_forstress);
    // keep track of which components have finished
    StressLevelComponents = [];
    StressLevelComponents.push(stresslevel_text);
    StressLevelComponents.push(stresslevel_keypress);
    StressLevelComponents.push(displaystressrating_text);
    StressLevelComponents.push(stress_slider);
    StressLevelComponents.push(StressLevelClock);
    StressLevelComponents.push(userMouse);
    StressLevelComponents.push(Stress_Button);
    StressLevelComponents.push(stresscontinue_text);


    for (const thisComponent of StressLevelComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

var keys;
var rating_forstress;
var stress_ratingvalue;
var gotValidClick;
var marker_pos;
var ratingvalue;
var buttonpress;
var finalmouseRT;
function StressLevelRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'StressLevel' ---
    // get current time
    t = StressLevelClock.getTime();
    frameN = frameN + 1;
    let buttonpress = userMouse.getPressed(); // read mouse state
      const xys = userMouse.getPos();
      userMouse.x.push(xys[0]); // add mouse coordinates to x/y list, in principle for data storage, but not implemented right now
      userMouse.y.push(xys[1]);
      userMouse.leftButton.push(buttonpress[0]); // store buttons in button list, likewise for storage
      userMouse.midButton.push(buttonpress[1]);
      userMouse.rightButton.push(buttonpress[2]);


    // *stresslevel_text* updates
    if (t >= 0.0 && stresslevel_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stresslevel_text.tStart = t;  // (not accounting for frame time here)
      stresslevel_text.frameNStart = frameN;  // exact frame index

      stresslevel_text.setAutoDraw(true);
      }

      // *stresslevel_keypress* updates
    if (t >= 0.0 && stresslevel_keypress.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stresslevel_keypress.tStart = t;  // (not accounting for frame time here)
      stresslevel_keypress.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { stresslevel_keypress.clearEvents(); });
    }

    // *stresscontinue_text* updates
    //  if (t >= 0.0 && stresscontinue_text.status === PsychoJS.Status.NOT_STARTED) {
    if (stresslevel_keypress.status === PsychoJS.Status.STARTED && stresscontinue_text.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        stresscontinue_text.tStart = t;  // (not accounting for frame time here)
        stresscontinue_text.frameNStart = frameN;  // exact frame index

        stresscontinue_text.setAutoDraw(true);
        Stress_Button.setAutoDraw(true);
        displaystressrating_text.setText('Click line');
        displaystressrating_text.setAutoDraw(true);
    }
    // // *stress_slider* updates
    if (t >= 0.0 && stress_slider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stress_slider.tStart = t;  // (not accounting for frame time here)
      stress_slider.frameNStart = frameN;  // exact frame index

      stress_slider.setAutoDraw(true);
    }






    // if (stresslevel_keypress.status === PsychoJS.Status.STARTED) {
    //   let theseKeys = stresslevel_keypress.getKeys({keyList: ['space'], waitRelease: false});
    //   _stresslevel_keypress_allKeys = _stresslevel_keypress_allKeys.concat(theseKeys);
    //   if (_stresslevel_keypress_allKeys.length > 0) {
    //     stresslevel_keypress.keys = _stresslevel_keypress_allKeys[_stresslevel_keypress_allKeys.length - 1].name;  // just the last key pressed
    //     stresslevel_keypress.rt = _stresslevel_keypress_allKeys[_stresslevel_keypress_allKeys.length - 1].rt;
    //     // a response ends the routine
    //     continueRoutine = false;
    //   }
    // }
    var _pj;
      function _pj_snippets(container) {
          function in_es6(left, right) {
              if (((right instanceof Array) || ((typeof right) === "string"))) {
                  return (right.indexOf(left) > (- 1));
              } else {
                  if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                      return right.has(left);
                  } else {
                      return (left in right);
                  }
              }
          }
          container["in_es6"] = in_es6;
          return container;
      }
      _pj = {};
      _pj_snippets(_pj);


      const validclicks = [1,2,3,4,5,6,7,8,9]
        ratingvalue = stress_slider.getMarkerPos();
          if (1 < ratingvalue && ratingvalue < 1.5) {
                stress_slider.setMarkerPos(1)
                stress_slider.setRating(1)
                displaystressrating_text.setText(1);
                displaystressrating_text.setAutoDraw(true);

          }

          else if (1.5 < ratingvalue && ratingvalue < 2.5) {
                stress_slider.setMarkerPos(2)
                stress_slider.setRating(2)
                displaystressrating_text.setText(2);
                displaystressrating_text.setAutoDraw(true);

          }
            else if (2.5 < ratingvalue && ratingvalue < 3.5) {
                stress_slider.setMarkerPos(3)
                stress_slider.setRating(3)
                displaystressrating_text.setText(3);
                displaystressrating_text.setAutoDraw(true);

          }
          else if (3.5 < ratingvalue && ratingvalue < 4.5) {
              stress_slider.setMarkerPos(4)
              stress_slider.setRating(4)
              displaystressrating_text.setText(4);
              displaystressrating_text.setAutoDraw(true);
            }
          else if (4.5 < ratingvalue && ratingvalue < 5.5) {
              stress_slider.setMarkerPos(5)
              stress_slider.setRating(5)
              displaystressrating_text.setText(5);
              displaystressrating_text.setAutoDraw(true);

        }
        else if (5.5 < ratingvalue && ratingvalue < 6.5) {
            stress_slider.setMarkerPos(6)
            stress_slider.setRating(6)
            displaystressrating_text.setText(6);
            displaystressrating_text.setAutoDraw(true);

      }
      else if (6.5 < ratingvalue && ratingvalue < 7.5) {
          stress_slider.setMarkerPos(7)
          stress_slider.setRating(7)
          displaystressrating_text.setText(7);
          displaystressrating_text.setAutoDraw(true);

    }
    else if (7.5 < ratingvalue && ratingvalue < 8.5) {
        stress_slider.setMarkerPos(8)
        stress_slider.setRating(8)
        displaystressrating_text.setText(8);
        displaystressrating_text.setAutoDraw(true);

  }
  else if (8.5 < ratingvalue && ratingvalue < 9) {
      stress_slider.setMarkerPos(9)
      stress_slider.setRating(9)
      displaystressrating_text.setText(9);
      displaystressrating_text.setAutoDraw(true);

}

            finalmouseRT = mouseClock.getTime(); // get mouse time, again for storage that is not implemented
            if (!buttonpress.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
              prevButtonState = buttonpress; //button state as of last frame, makes sure holding mouse down has not affected anything
              //debug code
              //console.log('new button state detected');
              if (buttonpress.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
                // check if the mouse was inside our 'clickable' objects
                gotValidClick = false;
                if (Stress_Button.contains(userMouse) && ratingvalue > 0) {
                  {gotValidClick = true};
                }
                if (gotValidClick === true) { // abort routine on response
                    continueRoutine = false;
                }
              }
            }




    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StressLevelComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

// var stresslevel;
function StressLevelRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'StressLevel' ---
    for (const thisComponent of StressLevelComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }

    function financial(x) {
                  return Number.parseFloat(x).toFixed(2);
                }
    // Run 'End Routine' code from stresslevelslider
    // stresslevel = stress_slider.getRating();
    entiretaskloop.addData("stress_level", Math.round(stress_slider.getMarkerPos()*10/10));

    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(stresslevel_keypress.corr, level);
    }
    psychoJS.experiment.addData('stresslevel_keypress.keys', stresslevel_keypress.keys);
    if (typeof stresslevel_keypress.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('stresslevel_keypress.rt', stresslevel_keypress.rt);
        routineTimer.reset();
        }

    stresslevel_keypress.stop();
    // the Routine "StressLevel" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}
//--- Prepare to start Routine 'End_Screen' ---
var t;
var frameN;
var continueRoutine;
var _end_screen_keys_allKeys;
var End_ScreenComponents;
function End_ScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date

    //--- Prepare to start Routine 'end_Screen' ---
    t = 0;
    end_screenclock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    end_screen_keys.keys = undefined;
    end_screen_keys.rt = undefined;
    _end_screen_keys_allKeys = [];
    // keep track of which components have finished
    End_ScreenComponents = [];
    End_ScreenComponents.push(end_screen);
    End_ScreenComponents.push(end_screen_keys);

    for (const thisComponent of End_ScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function End_ScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_screen_Screen' ---
    // get current time
    t = end_screenclock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame

    // *end_screen* updates
    if (t >= 0.0 && end_screen.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_screen.tStart = t;  // (not accounting for frame time here)
      end_screen.frameNStart = frameN;  // exact frame index

      end_screen.setAutoDraw(true);
    }


    // *end_screen_keys* updates
    if (t >= 0.0 && end_screen_keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_screen_keys.tStart = t;  // (not accounting for frame time here)
      end_screen_keys.frameNStart = frameN;  // exact frame index

      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { end_screen_keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { end_screen_keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { end_screen_keys.clearEvents(); });
    }

    if (end_screen_keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = end_screen_keys.getKeys({keyList: ['space'], waitRelease: false});
      _end_screen_keys_allKeys = _end_screen_keys_allKeys.concat(theseKeys);
      if (_end_screen_keys_allKeys.length > 0) {
        end_screen_keys.keys = _end_screen_keys_allKeys[_end_screen_keys_allKeys.length - 1].name;  // just the last key pressed
        end_screen_keys.rt = _end_screen_keys_allKeys[_end_screen_keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }

    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }

    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of End_ScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }

    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function End_ScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_Screen' ---
    for (const thisComponent of End_ScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(end_screen_keys.corr, level);
    }
    psychoJS.experiment.addData('end_screen_keys.keys', end_screen_keys.keys);
    if (typeof end_screen_keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('end_screen_keys.rt', end_screen_keys.rt);
        routineTimer.reset();
        }

    end_screen_keys.stop();
    // the Routine "end_Screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();

    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}



function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    }
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
   };
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  //  when they press space, redirect to choice task
  window.location.replace(weblink+= '?PROLIFIC_ID=' + expInfo['participant']);

  return Scheduler.Event.QUIT;
}
