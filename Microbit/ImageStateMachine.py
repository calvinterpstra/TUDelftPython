# Add your Python code here. E.g.
from microbit import *

t0_emotion = running_time()
emotionState = 0
dislpayState = Image.CONFUSED


def getTime_emotion():
    return running_time() - t0_emotion

def resetTime_emotion():
    global t0_emotion
    t0_emotion = running_time()

def setEmotion(image):
    global dislpayState
    dislpayState = image

def initEmotion(emotionState):
    resetTime_emotion()
    emotionState += 1
    return emotionState

def happy(emotionState):
    setEmotion(Image.HAPPY)
    if(getTime_emotion() > 2000):
        resetTime_emotion()
        emotionState += 1
    return emotionState

def sad(emotionState):
    setEmotion(Image.SAD)
    if(getTime_emotion() > 1000):
        resetTime_emotion()
        emotionState += 1
    return emotionState

def teardownEmotion(emotionState):
    resetTime_emotion()
    emotionState = 1
    return emotionState

emotionStates = {
    0: initEmotion,
    1: happy,
    2: sad,
    3: teardownEmotion
}

def emotionStateMachine(state):
    func = emotionStates.get(state)
    return func(state)

def commitDispayState():
    display.show(dislpayState)

while True:
    emotionState = emotionStateMachine(emotionState)
    commitDispayState()
    sleep(100)
