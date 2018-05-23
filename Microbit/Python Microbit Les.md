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
In elke *state* wordt er een actie uitgevoerd, dit is dus doormiddels van een `function`, of *functie* gedaan:

```python 
def mijnFunctie(invoerwaarde): # defineert een functie genoemd "mijnFunctie"
    uitvoerwaarde = invoerwaarde * 1 # Doet iets met de invoerwaarde
    return uitvoerwaarde # Geeft een niewe waarde terug
```

### Dictionaries:
Er moet een lijst van *states* bijgehouden worden samen met de naam van die *state*. Dus de naam is de *key* en de uitgevoerde functie is de *value*. Hiervoor gebruiken wij een `dictionary`:

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

Hiervoor is er wat code gegeven om mee te beginnen: (Voor deze les is het niet belangrijk te weeten exact wat `powerToAnalog` doet binnen de functie, alleen dat het functie nodig is om de servos aantedrijven)

```python 
from microbit import *

servoPowerState = {
    'right': 0,
    'left': 0
}

def powerToAnalog(power):
    if(power <= -100):
        return 45
    elif(power >= 100):
        return 105
    else:
        return power*0.3 + 75

def vooruit(power): # 
    servoPowerState['right'] = power
    servoPowerState['left'] = -power

def commitServoPowers():
    pin1.write_analog(powerToAnalog(servoPowerState.get('right')))
    pin2.write_analog(powerToAnalog(servoPowerState.get('left')))

```
