# Een Robot competitie op de Micro:bit in Python
Calvin Terpstra, Python programmeren masterclass, 30-5-2018

Met python op de Micro:bit kan jij zelf een robot competitie gaan programmeren! Dan kan je dus met je vrienden een competitie gaan doen van wie het beste een robot kan besturen. 

## Het competitie:
Het doel van het spel is om de robot om een paar obstakels te laten bewegen en zo dicht mogelijk op een doel terecht te komen. Het speelveld kan jij zelf gaan bedenken, en kan je ook veranderen en het zelfde code te gebruiken. 

## Belangrijke programmeer onderwerpen
Voordat je begint  programmeren in Python moeten wij een paar programmeer onderwerpen kennen.

### Functions:
Ik een paar *functies* gemaakt die jij kan gebruiken om makkelijk de robot te bewegen. Het is dus belangrijk te weten hoe jij dit kan gebruiken. Een *functie* werkt bijvoorbeeld zo:

```python 
def som(a, b): # Definieert een functie die a en b op gaan tellen
    return a + b # Geeft de som van a en b terug

print som(1,2) # Dit roept de functie aan, en geeft 3 terug 
```

### Lists en Dictionaries:
Wij gaan informatie uit *lijsten* en *dictionaries* lezen en gebruiken. Hier zijn er twee voorbeelden van een lijst, en een lijst van dictionaries. Je kan dus ook een dictionary in een lijst stoppen!

```python 
boodschappenlijst = ['kaas', 'pindakaas', 'hagelslag'] # Definieert een list

boodschappenlijst2 = [{'fruit1': 'appel', 'fruit2': 'banaan', 'fruit3': 'peer'},
                    {'beleg1': 'kaas', 'beleg2': 'pindakaas', 'beleg3': 'hagelslag'},
                    {'groenten1': 'sla', 'groenten2': 'komkommer', 'groenten3': 'paprika'}] # Definieert een list met meerdere dictionaries er in, bijvoorbeeld een boodschappenlijst gesorteerd op fruit, brood beleg, en groenten

print(boodschappenlijst[0]) # Print de eerste element: 'brood'
print(boodschappenlijst[1].get('beleg3')) # Print de element: 'hagelslag'
```

### Loops:
Wij gaan informatie uit een *list*, of *lijst*, lezen en gebruiken. Hiervoor heb jij een `for` loop nodig die er bijvoorbeeld alle elementen uit een boodschappenlijst uit gaat printen:

```python 
boodschappenlijst = ['kaas', 'pindakaas', 'hagelslag'] # Definieert een list
for voedsel in boodschappenlijst: # Loopt door elk element in de lijst
    print voedsel # Print de element
```


Hiermee zijn we nu klaar om aan de slag te gaan met een robot competitie programmeren!

## Deel 1: Beweging van de Micro:bit
Ik heb een paar functies voorbereid zodat jij makkelijker aan de gang kan gaan met de robot te laten bewegen:

```python 
from microbit import * # Beginnen de programma door alles vanuit de microbit library te importeren, dit is maar een keer nodig

# Gegeven functies:
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
    sleep(titijd*1000)

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

def stop(): # Stopt de robot
    pin1.write_analog(power_to_analog(0))
    pin2.write_analog(power_to_analog(0))
```

Om bijvoorbeeld de robot vooruit te laten bewegen en daarna te stoppen roep je de functies `vooruit` en `stop` aan. Probeer dit op de robot te draaien om te zien wat het doet!

```python
# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekent een gezicht op de robot omdat het leuk is
vooruit(100, 0.5) # Beweegt volle snelheid vooruit voor een halve seconde
stop() # Stopt nadat het klaar is met de beweging
```

Probeer nu zelf de robot achteruit te laten bewegen in plaats van vooruit.

## Deel 2: Meerdere Bewegingen
Als er iets in de weg licht van je robot, dan moet het er om heen kunnen manoeuvreren. Probeer de robot in deze pad te laten bewegen, vergeet niet te stoppen aan het einde, anders rijd de robot oneindg door! Voor nu hou ook alle bewegingen op volle kracht. (Hint: gebruik hiervoor `vooruit`, `rechts`, `links`, en `stop`)

```
           _____
          |     |
(start)___|  X  |___(eind)
```

Het zou er ongeveer zo uit moeten zien:

```python
# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekent een gezicht op de robot omdat het leuk is
vooruit(100, 0.8) # Beweegt volle snelheid vooruit voor een halve seconde
links(100, 0.4) # Beweegt volle snelheid links voor een halve seconde
vooruit(100, 0.8) # Beweegt volle snelheid vooruit voor een halve seconde
rechts(100, 0.4) # Beweegt volle snelheid rechts voor een halve seconde
vooruit(100, 0.8) # Beweegt volle snelheid vooruit voor een halve seconde
rechts(100, 0.4) # Beweegt volle snelheid rechts voor een halve seconde
vooruit(100, 0.8) # Beweegt volle snelheid vooruit voor een halve seconde
links(100, 0.4) # Beweegt volle snelheid links voor een halve seconde
vooruit(100, 0.8) # Beweegt volle snelheid vooruit voor een halve seconde
stop() # Stopt nadat het klaar is met de beweging
```

De robot die kan ook "voorzichtig" bewegen om een obstakel. Dit kan met een lagere percentage snelheid te gebruiken in de bewegingsfuncties. Bijvoorbeeld:

```python
# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekent een gezicht op de robot omdat het leuk is
vooruit(60, 0.5) # Beweegt met 60% snelheid vooruit voor een halve seconde
stop() # Stopt nadat het klaar is met de beweging
```

Probeer nu eerst snel naar en obstakel toe te bewegen, dan langzaam er om heen gaan, en dan weer snel naar de eind doel.

Nu heb jij je robot helemaal onder controle, en kan je jouw eigen baan maken en een competitie organiseren!

## Deel 3: Maar dit kan toch wel mooier?
Misschien heb je al gemerkt dat als jouw route wat langer wordt dan ga jij heel veel 'copy and pasten'. Dus dit kan makkelijker!

Maak eerst een lijst van de bewegingen die je wilt gaan doen. Dit heeft de informatie nodig: bewegingsfunctie, snelheid, en tijd voor elk element. Hiervoor kan jij een list van dictionaries maken, net als bij die boodschappenlijst.

Dit zou er dan zo uit kunnen zien:
```python 
bewegingen = [{'functie': vooruit, 'snelheid': 100, 'tijd': 0.8}, # element 1
            {'functie': rechts, 'snelheid': 60, 'tijd': 0.4}, # element 2
            {'functie': achteruit, 'snelheid': 70, 'tijd': 1}] # element 3
```

Om deze bewegingen nu uit te voeren hebben wij een for loop nodig die elke bewegings element uit kan voeren. Dit kan net zoals in de loop voorbeeld.

```python
# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekent een gezicht op de robot omdat het leuk is
for beweging in bewegingen:
    # voer functie uit
stop()
```

Elke beweging bestaat uit een `functie`, `snelheid`, en `tijd`. Om deze met de bijbehorende functie uit te voeren moeten wij de functie uit de dictionary pakken, en uit voeren met de correcte gegevens: 

```python
bewegingsfunctie = beweging.get('functie') # functie defineren
bewegingsfunctie(beweging.get('snelheid'), beweging.get('tijd')) # functie uitvoeren
```

Bij elkaar ziet het er dan zo uit:

```python
bewegingen = [{'functie': vooruit, 'snelheid': 100, 'tijd': 0.8},
            {'functie': rechts, 'snelheid': 60, 'tijd': 0.4},
            {'functie': achteruit, 'snelheid': 70, 'tijd': 1}]

# Zet hier de code die uitgevoerd moet worden
display.show(Image.HAPPY) # Tekent een gezicht op de robot omdat het leuk is
for beweging in bewegingen:
    bewegingsfunctie = beweging.get('functie')
    bewegingsfunctie(beweging.get('snelheid'), beweging.get('tijd'))
stop()
```

Merk dat je nu alleen nog de `bewegingen` lijst aan hoeft te passen om je robot te controleren!