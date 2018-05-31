# Add your Python code here. E.g.
from microbit import *

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

while True:
    display.show(Image.CLOCK1)
    forward(0)
    sleep(1000)
    display.show(Image.CLOCK2)
    forward(0)
    sleep(500)
    display.show(Image.CLOCK3)
    forward(0)
    sleep(1000)
    display.show(Image.CLOCK4)
    forward(0)
    sleep(500)
        
