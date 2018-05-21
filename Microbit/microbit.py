# Add your Python code here. E.g.
from microbit import *

t0 = running_time()
state = 0
servoPowerState = {
    'right': 75,
    'left': 75
}

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
    pin1.write_analog(powerToAnalog(power))
    pin2.write_analog(powerToAnalog(-power))
    # servoPowerState['right'] = power
    # servoPowerState['left'] = -power

def forward30():
    global state
    forward(30)
    display.show(Image.CLOCK2)
    if(getTime() > 500):
        resetTime()
        state += 1

def stop():
    global state
    forward(0)
    display.show(Image.CLOCK12)
    if(getTime() > 500):
        resetTime()
        state += 1

def back30():
    global state
    forward(-30)
    display.show(Image.CLOCK10)
    if(getTime() > 500):
        resetTime()
        state += 1

def init():
    global state
    resetTime()
    state += 1

def teardown():
    global state
    resetTime()
    state = 1

states = {
    0: init,
    1: forward30,
    2: stop,
    3: back30,
    4: stop,
    5: teardown
}

def stateMachine(state):
    func = states.get(state)
    func()

# def commitServoPowers():
#     pin1.write_analog(powerToAnalog(servoPowerState.get('right')))
#     pin2.write_analog(powerToAnalog(servoPowerState.get('left')))

while True:
    stateMachine(state)
        
