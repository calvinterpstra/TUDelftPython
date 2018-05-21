# Add your Python code here. E.g.
from microbit import *

t0 = running_time()

def getTime():
    return running_time() - t0

def resetTime():
    global t0
    t0 = running_time()

state = 0
while True:
    if(getTime() > 1000):
        resetTime()
        state += 1

    # if(t0 > 1000):
    #     display.show(Image.CLOCK11)

    # if(t0 > 8000):
    #     display.show(Image.CLOCK9)
    # if(running_time() > 8000):
    #     display.show(Image.CLOCK8)

    if(state == 0):
        display.show(Image.CLOCK1)
    elif(state == 1):
        display.show(Image.CLOCK2)
    elif(state == 2):
        display.show(Image.CLOCK3)
    elif(state == 3):
        display.show(Image.CLOCK4)
    elif(state == 4):
        display.show(Image.CLOCK5)
    elif(state == 5):
        display.show(Image.CLOCK6)
    elif(state == 6):
        display.show(Image.CLOCK7)
    else:
        display.show(Image.CLOCK12)
    
    
        
