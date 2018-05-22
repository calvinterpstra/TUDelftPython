# Add your Python code here. E.g.
from microbit import *

t0_motion = running_time()
t0_emotion = running_time()

servoPowerState = {
    'right': 0,
    'left': 0
}
dislpayState = Image.SAD

def getTime_motion():
    return running_time() - t0_motion

def resetTime_motion():
    global t0_motion
    t0_motion = running_time()

def getTime_emotion():
    return running_time() - t0_emotion

def resetTime_emotion():
    global t0_emotion
    t0_emotion = running_time()

def powerToAnalog(power):
    if(power <= -100):
        return 45
    elif(power >= 100):
        return 105
    else:
        return power*0.3 + 75

def forward(power):
    servoPowerState['right'] = power
    servoPowerState['left'] = -power

def turn(power):
    servoPowerState['right'] = power
    servoPowerState['left'] = power

def initMotion(state):
    resetTime_motion()
    state['motion'] += 1
    return state

def moveForward(state):
    forward(50)
    if(getTime_motion() > 800 or state['emotion'] != 1):
        resetTime_motion()
        state['motion'] += 1
    return state

def turnRight(state):
    turn(60)
    if(getTime_motion() > 500 or state['emotion'] != 1):
        resetTime_motion()
        state['motion'] += 1
    return state

def stop(state):
    forward(0)
    if(getTime_motion() > 1000 and state['emotion'] == 1):
        resetTime_motion()
        state['motion'] += 1
    return state

def moveBackward(state):
    forward(-30)
    if(getTime_motion() > 500 or state['emotion'] != 1):
        resetTime_motion()
        state['motion'] += 1
    return state

def turnLeft(state):
    turn(-40)
    if(getTime_motion() > 500 or state['emotion'] != 1):
        resetTime_motion()
        state['motion'] += 1
    return state

def teardownMotion(state):
    resetTime_motion()
    forward(0)
    state['motion'] = 1
    return state

motionStates = {
    0: initMotion,
    1: moveForward,
    2: turnRight,
    3: stop,
    4: moveForward,
    5: turnLeft,
    6: stop,
    7: teardownMotion
}

def motionStateMachine(state):
    func = motionStates.get(state['motion'])
    return func(state)['motion']

def commitServoPowers():
    pin1.write_analog(powerToAnalog(servoPowerState.get('right')))
    pin2.write_analog(powerToAnalog(servoPowerState.get('left')))

def setEmotion(image):
    global dislpayState
    dislpayState = image

def initEmotion(state):
    resetTime_emotion()
    state['emotion'] += 1
    return state

def happy(state):
    setEmotion(Image.HAPPY)
    if(getTime_emotion() > 2000):
        resetTime_emotion()
        state['emotion'] += 1
    return state

def sad(state):
    setEmotion(Image.SAD)
    if(getTime_emotion() > 1000):
        resetTime_emotion()
        state['emotion'] += 1
    return state

def confused(state):
    setEmotion(Image.CONFUSED)
    if(getTime_emotion() > 1000):
        resetTime_emotion()
        state['emotion'] += 1
    return state

def teardownEmotion(state):
    resetTime_emotion()
    state['emotion'] = 1
    return state

emotionStates = {
    0: initEmotion,
    1: happy,
    2: sad,
    3: confused,
    4: teardownEmotion
}

def emotionStateMachine(state):
    func = emotionStates.get(state['emotion'])
    return func(state)['emotion']

def commitDispayState():
    display.show(dislpayState)

state = {
    'motion': 0,
    'emotion': 0
}
while True:
    state['motion'] = motionStateMachine(state)
    state['emotion'] = emotionStateMachine(state)
    commitServoPowers()
    commitDispayState()
    sleep(100)