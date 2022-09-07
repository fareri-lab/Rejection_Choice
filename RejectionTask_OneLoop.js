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
  partneravatar = "Images/nerdemoji_nobackground.png";
}
if ((Partner === "Riley")) {
  partneravatar = "Images/sunglassemoji_nobackground.png";
} else {
  if ((Partner === "Charlie")) {
      partneravatar = "Images/smilingemoji.png";
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
if ((! _pj.in_es6(TrialNumber, [1, 31, 61]))) {
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
if ((! _pj.in_es6(TrialNumber, [1, 31, 61]))) {
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
routineTimer.add(3.000000);
//routineTimer.add(parseFloat(Waiting));
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
frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
  fdbkimage = "Images/thumbsup.png";
} else {
  if ((Feedback === "did not like")) {
      fdbkimage = "Images/thumbsdown.png";
  }
}

// Routines running outside a loop should always advance the datafile row
if (currentLoop === psychoJS.experiment) {
psychoJS.experiment.nextEntry(snapshot);
}
return Scheduler.Event.NEXT;
}
}


// var WaitingforfeedbackComponents;
// function WaitingforfeedbackRoutineBegin(snapshot) {
//   return async function () {
//     TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
// 
//     //--- Prepare to start Routine 'Waitingforfeedback' ---
//     t = 0;
//     WaitingforfeedbackClock.reset(); // clock
//     frameN = -1;
//     continueRoutine = true; // until we're told otherwise
//     routineTimer.add(5.000000);
//     // update component parameters for each repeat
//     // keep track of which components have finished
//     WaitingforfeedbackComponents = [];
//     WaitingforfeedbackComponents.push(waiting_text);
// 
//     for (const thisComponent of WaitingforfeedbackComponents)
//       if ('status' in thisComponent)
//         thisComponent.status = PsychoJS.Status.NOT_STARTED;
//     return Scheduler.Event.NEXT;
//   }
// }
// 
// 
// function WaitingforfeedbackRoutineEachFrame() {
//   return async function () {
//     //--- Loop for each frame of Routine 'Waitingforfeedback' ---
//     // get current time
//     t = WaitingforfeedbackClock.getTime();
//     frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
//     // update/draw components on each frame
// 
//     // *waiting_text* updates
//     if (t >= 0.0 && waiting_text.status === PsychoJS.Status.NOT_STARTED) {
//       // keep track of start time/frame for later
//       waiting_text.tStart = t;  // (not accounting for frame time here)
//       waiting_text.frameNStart = frameN;  // exact frame index
// 
//       waiting_text.setAutoDraw(true);
//     }
// 
//     frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
//     if (waiting_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
//       waiting_text.setAutoDraw(false);
//     }
//     // check for quit (typically the Esc key)
//     if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
//       return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
//     }
// 
//     // check if the Routine should terminate
//     if (!continueRoutine) {  // a component has requested a forced-end of Routine
//       return Scheduler.Event.NEXT;
//     }
// 
//     continueRoutine = false;  // reverts to True if at least one component still running
//     for (const thisComponent of WaitingforfeedbackComponents)
//       if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
//         continueRoutine = true;
//         break;
//       }
// 
//     // refresh the screen if continuing
//     if (continueRoutine && routineTimer.getTime() > 0) {
//       return Scheduler.Event.FLIP_REPEAT;
//     } else {
//       return Scheduler.Event.NEXT;
//     }
//   };
// }
// 
// 
// function WaitingforfeedbackRoutineEnd(snapshot) {
//   return async function () {
//     //--- Ending Routine 'Waitingforfeedback' ---
//     for (const thisComponent of WaitingforfeedbackComponents) {
//       if (typeof thisComponent.setAutoDraw === 'function') {
//         thisComponent.setAutoDraw(false);
//       }
//     }
//     // Routines running outside a loop should always advance the datafile row
//     if (currentLoop === psychoJS.experiment) {
//       psychoJS.experiment.nextEntry(snapshot);
//     }
//     return Scheduler.Event.NEXT;
//   }
// }
// 

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
let continueRoutine = true;
t = 0;
conditionalBlank.setText('');
ChoiceClock.reset(); // clock
frameN = -1;
continueRoutine = true; // until we're told otherwise
routineTimer.add(10.000000);
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
  computer_text.setColor(new util.Color("white"));
} else {
  if ((choice_keys.keys === "s")) {
      selfrunOrNot = 1;
      comprunOrNot = 0;
      self_text.setColor(new util.Color("white"));
  } else {
      selfrunOrNot = 0;
      comprunOrNot = 0;
  }
}

// update the trial handler
if (currentLoop instanceof MultiStairHandler) {
currentLoop.addResponse(choice_keys.corr, level);
}
psychoJS.experiment.addData('choice_keys.keys', choice_keys.keys);
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
routineTimer.add(6.000000);
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

frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
if (Block1_facedowncard.status === PsychoJS.Status.STARTED && t >= frameRemains) {
Block1_facedowncard.setAutoDraw(false);
}

// *computerresponse* updates
if (t >= 2 && computerresponse.status === PsychoJS.Status.NOT_STARTED) {
// keep track of start time/frame for later
computerresponse.tStart = t;  // (not accounting for frame time here)
computerresponse.frameNStart = frameN;  // exact frame index

computerresponse.setAutoDraw(true);
}

frameRemains = 2 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

const trials = [30,60,90]

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
// number of completed frames (so 0 is the first frame)
// update/draw components on each frame
// Run 'Each Frame' code from saliencyrating_code
// where keys code was originally


// start_position = salience_slider.markerPos

// new_position = salience_slider.getcurrentmarkerppos()
// 
// if new_position != start_position:
//   marker = Math.round(salience_slider.getMarkerPos())
//   displayrating_text.setText(marker);
//   salience_slider.setMarkerPos(marker)
// 

// // // *salience_slider* updates
// if (t >= 0.0 && salience_slider.status === PsychoJS.Status.NOT_STARTED) {
//   // keep track of start time/frame for later
//   salience_slider.tStart = t;  // (not accounting for frame time here)
//   salience_slider.frameNStart = frameN;  // exact frame index
// 
//   salience_slider.setAutoDraw(true);
// }

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

// if (key_resp.status === PsychoJS.Status.STARTED) {
//   let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
//   _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
//   if (_key_resp_allKeys.length > 0) {
//     key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
//     key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
//     // a response ends the routine
//     continueRoutine = false;
// 
//   } else {
//     continueRoutine = true;
// 
//   }
// }

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




//  *displayrating_text* updates
// if (t >= 0.0 && displayrating_text.status === PsychoJS.Status.NOT_STARTED) {
//   // keep track of start time/frame for later
//   displayrating_text.tStart = t;  // (not accounting for frame time here)
//   displayrating_text.frameNStart = frameN;  // exact frame index
//   //displayrating_text.setText(salience_slider.getMarkerPos());
//   displayrating_text.setAutoDraw(true);
// 
// }
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
// salience_slider.setAutoDraw(true);


//     keys = psychoJS.eventManager.getKeys();
// //    displayrating_text.setText(Math.round(salience_slider.getMarkerPos(), 1));
// 
//     if (keys.length) {
//         if (_pj.in_es6("left", keys)) {
//             salience_slider.markerPos = (salience_slider.markerPos - 1);
//             rating_forsalience = salience_slider.getRating();
//             displayrating_text.setText(Math.round(salience_slider.getMarkerPos()));
//             salience_slider.setMarkerPos(Math.round(salience_slider.getMarkerPos()))
// 
//         } else {
//             if (_pj.in_es6("right", keys)) {
//                 salience_slider.markerPos = (salience_slider.markerPos + 1);
//                 rating_forsalience = salience_slider.getRating();
//                 displayrating_text.setText(Math.round(salience_slider.getMarkerPos()));
//                 salience_slider.setMarkerPos(Math.round(salience_slider.getMarkerPos()))
//             }
//         }
//     }

// const mouseInfo = this.psychoJS.eventManager.getMouseInfo();
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

// psychoJS.experiment.addData('saliencerating', financial(salience_slider.getRating())); //test
          // psychoJS.experiment.addData('pracScale.rt', userMouse.getPos()); //test
          // psychoJS.experiment.addData('saliencemouse.rt', pracfinalmouseRT);
// Run 'End Routine' code from saliencyrating_code
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
const trials = [30,60,90]

if (trials.includes(TrialNumber) == true) {
continueRoutine = true;

} else {
continueRoutine = false;
}
stressleveltext = `Please rate your current stress level.

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
// number of completed frames (so 0 is the first frame)
// update/draw components on each frame
// Run 'Each Frame' code from stresslevelslider
// var _pj;
// function _pj_snippets(container) {
//     function in_es6(left, right) {
//         if (((right instanceof Array) || ((typeof right) === "string"))) {
//             return (right.indexOf(left) > (- 1));
//         } else {
//             if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
//                 return right.has(left);
//             } else {
//                 return (left in right);
//             }
//         }
//     }
//     container["in_es6"] = in_es6;
//     return container;
// }
// _pj = {};
// _pj_snippets(_pj);
// stress_slider.draw();
// keys = psychoJS.eventManager.getKeys();
// displaystressrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
// if (keys.length) {
//     if (_pj.in_es6("left", keys)) {
//         stress_slider.markerPos = (stress_slider.markerPos - 0.1);
//         rating_forstress = stress_slider.getRating();
//         displayrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
//     } else {
//         if (_pj.in_es6("right", keys)) {
//             stress_slider.markerPos = (stress_slider.markerPos + 0.1);
//             rating_forstress = stress_slider.getRating();
//             displayrating_text.setText(Math.round(stress_slider.getMarkerPos(), 1));
//         }
//     }
// }
// 

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
// salience_slider.setAutoDraw(true);


// keys = psychoJS.eventManager.getKeys();
//    displayrating_text.setText(Math.round(salience_slider.getMarkerPos(), 1));

// if (keys.length) {
//     if (_pj.in_es6("left", keys)) {
//         stress_slider.markerPos = (stress_slider.markerPos - 1);
//         rating_forstress = stress_slider.getRating();
//         displaystressrating_text.setText(Math.round(stress_slider.getMarkerPos()));
//         stress_slider.setMarkerPos(Math.round(stress_slider.getMarkerPos()))
// 
//     } else {
//         if (_pj.in_es6("right", keys)) {
//             stress_slider.markerPos = (stress_slider.markerPos + 1);
//             rating_forstress = stress_slider.getRating();
//             displaystressrating_text.setText(Math.round(stress_slider.getMarkerPos()));
//             stress_slider.setMarkerPos(Math.round(stress_slider.getMarkerPos()))
//         }
//     }
// }
// 

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

// *displaystressrating_text* updates
// if (t >= 0.0 && displaystressrating_text.status === PsychoJS.Status.NOT_STARTED) {
//   // keep track of start time/frame for later
//   displaystressrating_text.tStart = t;  // (not accounting for frame time here)
//   displaystressrating_text.frameNStart = frameN;  // exact frame index
// 
//   displaystressrating_text.setAutoDraw(true);





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
//window.location.replace(weblink);

return Scheduler.Event.QUIT;
}    
