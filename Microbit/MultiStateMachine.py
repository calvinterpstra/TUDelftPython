# Add your Python code here. E.g.
from microbit import *

t0_motion = running_time()
t0_emotion = running_time()
motionState = 0
emotionState = 0
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

def initMotion():
    global motionState
    resetTime_motion()
    motionState += 1

def moveForward():
    global motionState
    forward(50)
    if(getTime_motion() > 800):
        resetTime_motion()
        motionState += 1

def turnRight():
    global motionState
    turn(60)
    if(getTime_motion() > 500):
        resetTime_motion()
        motionState += 1

def stop():
    global motionState
    forward(0)
    if(getTime_motion() > 1000):
        resetTime_motion()
        motionState += 1

def moveBackward():
    global motionState
    forward(-30)
    if(getTime_motion() > 500):
        resetTime_motion()
        motionState += 1

def turnLeft():
    global motionState
    turn(-40)
    if(getTime_motion() > 500):
        resetTime_motion()
        motionState += 1

def teardownMotion():
    global motionState
    resetTime_motion()
    forward(0)
    motionState = 1

motionStates = {
    0: initMotion,
    1: moveForward,
    2: turnRight,
    3: stop,
    4: moveBackward,
    5: turnLeft,
    6: stop,
    7: moveForward,
    8: teardownMotion
}

def motionStateMachine(state):
    func = motionStates.get(state)
    func()

def commitServoPowers():
    pin1.write_analog(powerToAnalog(servoPowerState.get('right')))
    pin2.write_analog(powerToAnalog(servoPowerState.get('left')))

def setEmotion(image):
    global dislpayState
    dislpayState = image

def initEmotion():
    global emotionState
    resetTime_emotion()
    emotionState += 1

def happy():
    global emotionState
    setEmotion(Image.HAPPY)
    if(getTime_emotion() > 2000):
        resetTime_emotion()
        emotionState += 1

def sad():
    global emotionState
    setEmotion(Image.SAD)
    if(getTime_emotion() > 1000):
        resetTime_emotion()
        emotionState += 1

def confused():
    global emotionState
    setEmotion(Image.CONFUSED)
    if(getTime_emotion() > 1000):
        resetTime_emotion()
        emotionState += 1

def teardownEmotion():
    global emotionState
    resetTime_emotion()
    emotionState = 1

emotionStates = {
    0: initEmotion,
    1: happy,
    2: sad,
    3: confused,
    4: teardownEmotion
}

def emotionStateMachine(state):
    func = emotionStates.get(state)
    func()

def commitDispayState():
    display.show(dislpayState)

while True:
    motionStateMachine(motionState)
    emotionStateMachine(emotionState)
    commitServoPowers()
    commitDispayState()
    sleep(100)
        
