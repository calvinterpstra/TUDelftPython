from microbit import * # Beginnen de programma door alles vanuit de microbit library te importeren, dit is maar een keer nodig

def power_to_analog(power):
    if(power <= -100):
        return 45
    elif(power >= 100):
        return 105
    else:
        return power*0.3 + 75

def vooruit(snelheid, tijd): # Beweegt de robot vooruit met een snelheid voor een hoeveelheid tijd
    pin1.write_analog(power_to_analog(snelheid))
    pin2.write_analog(power_to_analog(-snelheid))
    sleep(tijd*1000)

def achteruit(snelheid, tijd): # Beweegt de robot achteruit met een snelheid voor een hoeveelheid tijd
    pin1.write_analog(power_to_analog(-snelheid))
    pin2.write_analog(power_to_analog(snelheid))
    sleep(tijd*1000)

def rechts(snelheid, tijd): # Draait de robot rechts met een snelheid voor een hoeveelheid tijd
    pin1.write_analog(power_to_analog(snelheid))
    pin2.write_analog(power_to_analog(snelheid))
    sleep(tijd*1000)

def links(snelheid, tijd): # Draait de robot links met een snelheid voor een hoeveelheid tijd
    pin1.write_analog(power_to_analog(-snelheid))
    pin2.write_analog(power_to_analog(-snelheid))
    sleep(tijd*1000)

def stop():
    pin1.write_analog(power_to_analog(0))
    pin2.write_analog(power_to_analog(0))

# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekend een gezicht op het robot
vooruit(100, 0.5)
stop()
        
