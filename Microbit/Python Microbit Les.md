# Simpel State Machine op de Micro:bit in Python
Calvin Terpstra, Python Programeren masterclass, 26-5-2018

## Wat is een State Machine?
Een *State Machine* houd bij de *state*, of toestand, van je programma. Op basis van bepaalde condities stapt het van een *state* naar een andere.

State Machines kunnen erg nuttig zijn in het programeren van een robot. De *state* waar de robot in zit is de actie die die uit moet voeren. Met gebruik van sensor data, tijd, en/of input van een controller kan het een beslissing nemen om naar een niewe *state* te gaan, of in andere woorden: de robot beslist wat te doen op basis van dingen die het voelt of ziet.

Een State Machine kan ook wel erg complex worden. Het kan tussen elke *state* springen, of zelfs merdere states tegelijk uitvoeren.

## Wat gaan we doen met de State machine?
Wij beginnen met een simpele *lineare* State Machine, en bouwen op tot een programma die twee states tegelijk bijhoud en afankelijk van elkaar zijn. Hiermee laten we de Micro:bit rond rijden op een voorgeprogameerde route en op basis van de "emotie" van de robot.

## Belangrijke programeer onderwerpen
Om een simpele State Machine te programeeren in Python moeten wij een paar programeer onderwerpen leren kennen.

### Loops:
Om een State Machine te laten "draaien" hebben wij een *loop* nodig die dus elke fractie van een seconde de opdrachten uit kan voeren. Hiervoor gebruiken wij een `while` loop, die er zo uit gaat zien:

```python 
while True:
    # Uitvoering van state machite
    sleep(100) # Elke 100 milliseconden uitvoeren
```

### Functions:
In elke *state* wordt er een actie uitgevoerd, dit is dus doormiddels van een *function*, of *functie* gedaan:

```python 
def mijnFunctie(invoerwaarde): # defineert een functie genoemd "mijnFunctie"
    uitvoerwaarde = invoerwaarde * 1 # Doet iets met de invoerwaarde
    return uitvoerwaarde # Geeft een niewe waarde terug
```

### Conditionals:
Ik elke state comt ook een *conditional statement*, bijvoorbeeld een `if` statement:

```python 
if(getTime() > 2000):
    # Doet iets
elif(getTime() > 1000):
    # Doet iets anders
else:
    # Doet nog iets anders
```

### Dictionaries:
Er moet een lijst van *states* bijgehouden worden samen met de naam van die *state*. Dus de naam is de *key* en de uitgevoerde functie is de *value*. Hiervoor gebruiken wij een *dictionary*:

```python 
states = { # Maakt een dinctionary genoemd "states"
    state0: initializatie, # key: value, of naam: functie
    state1: vooruit,
    state2: stop,
    state3: achteruit,
    state4: afbreaken
}
```

Hiermee zijn we nu kaar om aan de slag te gaan met een State Machine programeren!

## Deel 1: Beweging en Display van de Micro:bit
Voor dat we echt in de werking van een state machine gaan duiken, gaan we eerst even een paar functies maken die wij uit kunnen voeren in een *state*

Hiervoor is er wat code gegeven om de servos aantedrijven: (Voor deze les is het niet belangrijk te weeten exact wat `powerToAnalog` doet binnen de functie, alleen dat het functie nodig is om de servos aantedrijven)

```python 
from microbit import * # Beginnen de programma door alles vanuit de microbit library te importeren, dit is maar een keer nodig

fysiekeToestand = { # De fysieke toestand van de micro:bit
    'rechterServoPower': 0,
    'linkerServoPower': 0,
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

def commitFysiekeToestand(): # Stuurt signaal uit de servo state naar servos
    pin1.write_analog(powerToAnalog(fysiekeToestand.get('rechterServoPower')))
    pin2.write_analog(powerToAnalog(fysiekeToestand.get('linkerServoPower')))

```

Om de Micro:bit vooruit te laten bewegen roepen wij de functie aan: `vooruit(100)` (beweegt vooruit met 100% vermogen), of om te draaien: `draaien(-50)` (draait links met 50% vermogen)

Wij kunnen ook afbeeldingen op de display van de Micro:bit afbeelden, bijvoorbeeld door deze functies:

```python
fysiekeToestand = { # De fysieke toestand van de micro:bit
    'dislpayState': Image.HAPPY
}

def instelAfbeelding(image): # Update de state van het display met een afbeelding
    fysiekeToestand['dislpayState'] = image

def commitFysiekeToestand(): # Toond een afbeelding op het display
    display.show(fysiekeToestand.get('dislpayState'))
```

Om iets aftebeelden moeten wij de functie `instelAfbeelding` aanroepen bijvoorbeeld zo: `instelAfbeelding(Image.SAD)`. Hier mee toond het display een sad-face aan. (Hier kan je een lijt vinden van alle andere Images: http://microbit-micropython.readthedocs.io/en/latest/tutorials/images.html)

Wij kunnen ook onze iegen Image aanmaken: 
```python
boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "09990")
```

## Deel 2: Timing
Het is belangrijk om de tijd bij te houden om te beslissen hoe lang een *state* uitgevored moet worden. Hierbij gebruiken wij deze functies:

```python
t0 = running_time() # De tijd waarop ons timer start

def getTime(): # Geeft de tijd van onze timer
    return running_time() - t0

def resetTime(): # Reset onze timer
    global t0
    t0 = running_time()
```

Om de verlopde tijd te vinden roepen wij de functie aan: `getTime()`. Waneer wij het tijdt willen reseten, kan dat met de functie `resetTime()`. Deze tijd is in *milliseconden*, dus de tijd (`getTime()`) na een seconde is 1000.

## Deel 3: Simpele Lineare State Machine
Nu gaan we de Mirco:bit in een vierkante baan laten bewegen om te begrijpen hoe wij een state machine kunnen gebruiken.

Elke beweging wordt zijn eigen *state*. Eerst gaan wij een dictionary aan maken met alle states die wij gaan gebruiken:

```python
states = {
    0: initializatie,
    1: beweegVooruit,
    2: stop,
    3: draaiRechts,
    4: afbreaken
}
```
Een state machine begint en eindigd altijd met een initializatie en afbreak van zichzelf. Dit is belangrijk omdat er voorbereid kan worden en processen gestopped kunnen worden om in een goed draaiende programma te passen. Dit betekend ook dat een zo een set van *states* zich zelf een *state* kan zijn.

Nu moeten wij deze states aan gaan roepen, dit doen we zo:

```python
def stateMachine(state): # Functie waarmee de states worden geroepen
    func = states.get(state) # Pakt de functie die bij de huidige state hoort
    return func(state) # Elke state geeft de volgende state aan als return waarde

state = 0 # Begin state
while True:
    state = stateMachine(state) # Update en voerd de huidige state uit
    commitServoPowers() # Nu worden de servos pas echt aangedreven
    sleep(100) # Geeft tijd om alles uit te voeren
```

In een state bestaat dus heel simpeg geziet uit twee delen: een functie die het uit voort, en een *conditional statement* die beslist waneer die klaar is om naar de volgende state te gaan. Voor de `beweegVooruit` state ziet dit er zo uit:

```python
def beweegVooruit(state): # Defineert functie voor state
    vooruit(50) # Beweeg vooruit met 50%
    if(getTime() > 800): # Als de tijd > 0.8 seconden is...
        resetTime() # Timer resetten
        state += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn (eerst vaak het huidige)
```

Gegeven zijn ook de initializatie en afbreaken states:

```python
def initializatie(state): # Defineert functie voor state
    resetTime() # Timer resetten
    state += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn

def afbreaken(state): # Defineert functie voor state
    resetTime() # Timer resetten
    forward(0) # Stop servos (zet vermogen naar 0%)
    state = 1 # State terug naar het begin zetten om oneindig door de states te loopen (na de initializatie)
    return state # Geeft door wat de volgende state moet zijn
```

Probeer nu zelf ook de `stop` en `draaiRechts` states te programeren, en alles in een draaiende programma te zetten. Het zou in een (bijna) vierkante route bewegen.

En nu ziet het zo uit met alles bij elkaar:

```python
from microbit import * # Beginnen de programma door alles vanuit de microbit library te importeren, dit is maar een keer nodig

t0 = running_time() # De tijd waarop ons timer start

def getTime(): # Geeft de tijd van onze timer
    return running_time() - t0

def resetTime(): # Reset onze timer
    global t0
    t0 = running_time()

fysiekeToestand = { # De fysieke toestand van de micro:bit
    'rechterServoPower': 0,
    'linkerServoPower': 0,
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

def commitFysiekeToestand(): # Stuurt signaal uit de servo state naar servos
    pin1.write_analog(powerToAnalog(fysiekeToestand.get('rechterServoPower')))
    pin2.write_analog(powerToAnalog(fysiekeToestand.get('linkerServoPower')))

def initializatie(state): # Defineert functie voor state
    resetTime() # Timer resetten
    state += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn

def afbreaken(state): # Defineert functie voor state
    resetTime() # Timer resetten
    forward(0) # Stop servos (zet vermogen naar 0%)
    state = 1 # State terug naar het begin zetten om oneindig door de states te loopen (na de initializatie)
    return state # Geeft door wat de volgende state moet zijn

def beweegVooruit(state): # Defineert functie voor state
    vooruit(50) # Beweeg vooruit met 50%
    if(getTime() > 800): # Als de tijd > 0.8 seconden is...
        resetTime() # Timer resetten
        state += 1 # Naar de volgende state gaan
    return state # Geeft door wat de volgende state moet zijn (eerst vaak het huidige)

def stop(state):
    vooruit(0) #  Stop servos (zet vermogen naar 0%)
    if(getTime() > 800): # Hoeft niet 0.8 seconden te zijn, is voorbeeld
        resetTime()
        state += 1
    return state # Geeft door wat de volgende state moet zijn (eerst vaak het huidige)

def draaiRechts(state):
    draaien(60) # Draai met 60%
    if(getTime() > 500): # Hoeft niet 0.5 seconden te zijn, is voorbeeld
        resetTime()
        state += 1
    return state

states = { # Maakt een dictionary voor alle states
    0: initializatie,  # Key: value, of naam: functie
    1: beweegVooruit,
    2: stop,
    3: draaiRechts,
    4: afbreaken
}

def stateMachine(state): # Functie waarmee de states worden geroepen
    func = states.get(state) # Pakt de functie die bij de huidige state hoort
    return func(state) # Elke state geeft de volgende state aan als return waarde

state = 0 # Begin state
while True:
    state = stateMachine(state) # Update en voerd de huidige state uit
    commitFysiekeToestand() # Nu worden de servos pas echt aangedreven
    sleep(100) # Geeft tijd om alles uit te voeren
```
Dit kan je nu op de Micro:bit draaien! Doe dit door naar de python editor (https://python.microbit.org/v/1) te gaan, jouw code loaden, en dan downloaden naar de Micro:bit

Probeer nu ook helemaal zelf een lineare State Machine te maken die een paar verschillende afbeeldingen toond. 

## Deel 4: Gecombineerde State Machines
State machines kunnen ook veel colplexer (en leuker) zijn. Je kan zelfs meerdere parallel laten draaien, en ze ook afankelijk van elkaar maken!

Wij gaan dus nu een State Machine maken die twee states bijhoud: een beweging en een "emotie". De Micro:bit gaat alleen bewegen als het blij (happy) is, en stoppen als het verdrietig (sad) is.

Om dit te doen moeten wij een paar dingen van onze lineare state machine aanpassen. Om dat wij nu twee states boumoeten houden, moet onse *state* variabel informatie bijhouden voor twee state machines, een for beweging, en een voor emotie:

```python
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
```
Ook moeten er twee timers zijn:

```python
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
```

Binnen de state functies moeten wij nu ook anders om gaan met de state omdat het een dictionary is.

Het moet er bij voorbeeld zo uit zien:

```python
def blij(state):
    instelAfbeelding(Image.HAPPY)
    if(getTimeEmotie() > 2000): # Blij voor 2 seconden
        resetTimeEmotie()
        state['emotie'] += 1
    return state
```

Probeer nu zelf ook de rest van de states te programeren, en vergeet niet dat de *conditional* voor de bewegingen ook naar de emotie state moeten kijken. Hieronder staan de niewe states gedefineerd:

```python
bewegingStates = {
    0: bewegingInitializatie,
    1: beweegVooruit,
    2: stop,
    3: draaiRechts,
    4: stop,
    5: bewegingAfbreaken
}

emotieStates = {
    0: emotieInitializatie,
    1: blij,
    2: verwarred,
    3: verdrietig,
    4: verwarred,
    5: emotieAfbreaken
}
```
Nou dat alles samen is, kan je jouw programma op de Micro:bit draaien!
