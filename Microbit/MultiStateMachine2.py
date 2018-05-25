# Add your Python code here. E.g.
from microbit import * # Beginnen de programma door alles vanuit de microbit library te importeren, dit is maar een keer nodig

t0_beweging = running_time() # De tijd waarop ons beweging timer start
t0_emotie = running_time() # De tijd waarop ons emotie timer start

def getTimeBeweging(): # Geeft de tijd van onze beweging timer
    return running_time() - t0_beweging

def getTimeEmotie(): # Geeft de tijd van onze emotie timer
    return running_time() - t0_emotie

def resetTimeBeweging(): # Reset onze beweging timer
    global t0_beweging
    t0_beweging = running_time()

def resetTimeEmotie(): # Reset onze emotie timer
    global t0_emotie
    t0_emotie = running_time()

fysiekeToestand = { # De fysieke toestand van de micro:bit
    'rechterServoPower': 0,
    'linkerServoPower': 0,
    'dislpayState': Image.SAD
}

def powerToAnalog(power): # Zet +/- 0-100% vermogen (power) over naar analog input
    if(power <= -100):
        return 45
    elif(power >= 100):
        return 105
    else:
        return power*0.3 + 75

def vooruit(power): # Update de power state van de servos (om vooruit te rijden, - is achteruit)
    fysiekeToestand['rechterServoPower'] = power
    fysiekeToestand['linkerServoPower'] = -power

def draaien(power): # Update de power state van de servos (om reghts om te draaien, - is links om)
    fysiekeToestand['rechterServoPower'] = power
    fysiekeToestand['linkerServoPower'] = power

def instelAfbeelding(image): # Update de state van het display met een afbeelding
    fysiekeToestand['dislpayState'] = image

def commitFysiekeToestand(): # Stuurt signaal uit de servo state naar servos en toond een afbeelding op het display
    pin1.write_analog(powerToAnalog(fysiekeToestand.get('rechterServoPower')))
    pin2.write_analog(powerToAnalog(fysiekeToestand.get('linkerServoPower')))
    display.show(fysiekeToestand.get('dislpayState'))

def bewegingInitializatie(state): # Defineert functie voor state
    resetTimeBeweging() # Timer resetten
    state['beweging'] += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn

def bewegingAfbreaken(state): # Defineert functie voor state
    resetTimeBeweging() # Timer resetten
    vooruit(0) # Stop servos (zet vermogen naar 0%)
    state['beweging'] = 1 # State terug naar het begin zetten om oneindig door de states te loopen (na de initializatie)
    return state # Geeft door wat de volgende state moet zijn

def emotieInitializatie(state): # Defineert functie voor state
    resetTimeEmotie() # Timer resetten
    state['emotie'] += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn

def emotieAfbreaken(state): # Defineert functie voor state
    resetTimeEmotie() # Timer resetten
    state['emotie'] = 1 # State terug naar het begin zetten om oneindig door de states te loopen (na de initializatie)
    return state # Geeft door wat de volgende state moet zijn

def beweegVooruit(state): # Defineert functie voor state
    vooruit(100) # Beweeg vooruit met 50%
    if(getTimeBeweging() > 800 or state['emotie'] != 1): # Als de tijd > 0.8 seconden is of niet blij meer is...
        resetTimeBeweging() # Timer resetten
        state['beweging'] += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn (eerst vaak het huidige)

def stop(state):
    vooruit(0) # Stop servos (zet vermogen naar 0%)
    if(getTimeBeweging() > 800 and state['emotie'] == 1): # Als de tijd > 0.8 seconden is en blij is...
        resetTimeBeweging()
        state['beweging'] += 1
    return state # Geeft door wat de volgende state moet zijn (eerst vaak het huidige)

def draaiRechts(state):
    draaien(90) # Draai met 60%
    if(getTimeBeweging() > 500 or state['emotie'] != 1): # Als de tijd > 0.5 seconden is of niet blij meer is...
        resetTimeBeweging()
        state['beweging'] += 1
    return state

def blij(state):
    instelAfbeelding(Image.HAPPY)
    if(getTimeEmotie() > 2000): # Blij voor 2 seconden
        resetTimeEmotie()
        state['emotie'] += 1
    return state

def verdrietig(state):
    instelAfbeelding(Image.SAD)
    if(getTimeEmotie() > 1000): # Verdrietig voor 1 seconde
        resetTimeEmotie()
        state['emotie'] += 1
    return state

def verwarred(state):
    instelAfbeelding(Image.CONFUSED)
    if(getTimeEmotie() > 1000): # Verwarred voor 1 seconde
        resetTimeEmotie()
        state['emotie'] += 1
    return state

bewegingStates = { # Maakt een dictionary voor alle beweging states
    0: bewegingInitializatie,  # key: value, of naam: functie
    1: beweegVooruit,
    2: stop,
    3: draaiRechts,
    4: stop,
    5: bewegingAfbreaken
}

emotieStates = { # Maakt een dictionary voor alle emotie states
    0: emotieInitializatie,  # key: value, of naam: functie
    1: blij,
    2: verwarred,
    3: verdrietig,
    4: verwarred,
    5: emotieAfbreaken
}

def bewegingStateMachine(state): # Functie waarmee de states worden geroepen
    func = bewegingStates.get(state['beweging']) # Pakt de functie die bij de huidige state hoort
    return func(state)['beweging'] # Elke state geeft de volgende state aan als return waarde

def emotieStateMachine(state): # Functie waarmee de states worden geroepen
    func = emotieStates.get(state['emotie']) # Pakt de functie die bij de huidige state hoort
    return func(state)['emotie'] # Elke state geeft de volgende state aan als return waarde

state = {  # Begin state (Dit is nu een dictionary met twee states)
    'beweging': 0,
    'emotie': 0
}
while True:
    state['beweging'] = bewegingStateMachine(state) # Update en voerd de huidige state uit
    state['emotie'] = emotieStateMachine(state) # Update en voerd de huidige state uit
    commitFysiekeToestand() # Nu worden de servos pas echt aangedreven en afbeelding pas echt afgebeeld
    sleep(100) # Geeft tijd om alles uit te voeren
