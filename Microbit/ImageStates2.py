# Add your Python code here. E.g.
from microbit import *

t0 = running_time()
motionState = 0
servoPowerState = {
    'right': 0,
    'left': 0
}
dislpayState = Image.CONFUSED

def getTime():
    return running_time() - t0

def resetTime():
    global t0
    t0 = running_time()

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

def setEmotion(image):
    global dysplayState
    dysplayState = image

def turn(power):
    servoPowerState['right'] = power
    servoPowerState['left'] = power

def init():
    global motionState
    resetTime()
    motionState += 1

def moveForward():
    global motionState
    forward(50)
    display.show(Image.CLOCK2)
    if(getTime() > 800):
        resetTime()
        motionState += 1

def turnRight():
    global motionState
    turn(60)
    display.show(Image.CLOCK5)
    if(getTime() > 500):
        resetTime()
        motionState += 1

def stop():
    global motionState
    forward(0)
    display.show(Image.CLOCK12)
    if(getTime() > 1000):
        resetTime()
        motionState += 1

def moveBackward():
    global motionState
    forward(-30)
    display.show(Image.CLOCK10)
    if(getTime() > 500):
        resetTime()
        motionState += 1

def turnLeft():
    global motionState
    turn(-40)
    # display.show(Image.CLOCK7)
    dislpayState
    if(getTime() > 500):
        resetTime()
        motionState += 1

def teardown():
    global motionState
    resetTime()
    forward(0)
    motionState = 1

motionStates = {
    0: init,
    1: moveForward,
    2: turnRight,
    3: stop,
    4: moveBackward,
    5: turnLeft,
    6: stop,
    7: moveForward,
    8: teardown
}

def motionStateMachine(state):
    func = motionStates.get(state)
    func()

def commitServoPowers():
    pin1.write_analog(powerToAnalog(servoPowerState.get('right')))
    pin2.write_analog(powerToAnalog(servoPowerState.get('left')))

def commitDispayState():
    display.show(dislpayState)

while True:
    motionStateMachine(motionState)
    # commitServoPowers()
    commitDispayState()
    sleep(100)
        
