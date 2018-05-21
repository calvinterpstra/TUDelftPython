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
    forward(0)
    display.show(Image.CLOCK1)
    sleep(300)
    forward(10)
    display.show(Image.CLOCK2)
    sleep(300)
    forward(20)
    display.show(Image.CLOCK3)
    sleep(300)
    forward(30)
    display.show(Image.CLOCK4)
    sleep(300)
    forward(40)
    display.show(Image.CLOCK5)
    sleep(300)
    forward(60)
    display.show(Image.CLOCK6)
    sleep(300)
    forward(100)
    display.show(Image.CLOCK7)
    sleep(300)
    forward(50)
    display.show(Image.CLOCK8)
    sleep(300)
    forward(20)
    display.show(Image.CLOCK9)
    sleep(300)
    forward(0)
    display.show(Image.CLOCK10)
    sleep(300)
    forward(-20)
    display.show(Image.CLOCK11)
    sleep(300)
    forward(-50)
    display.show(Image.CLOCK12)
    sleep(300)
    forward(-100)
    display.show(Image.CLOCK1)
    sleep(300)
    forward(-50)
    display.show(Image.CLOCK2)
    sleep(300)
    forward(-20)
    display.show(Image.CLOCK3)
    sleep(300)
    forward(-10)
    display.show(Image.CLOCK4)
    sleep(300)
        
