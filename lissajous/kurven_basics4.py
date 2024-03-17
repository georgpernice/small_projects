##Ziele:
##
##Turtle springt bisher zwischen dem Kreis hin/her
##da sie zu langsam.
##
##Tracer schien problematisch, daher vllt ondrag durch Tasten Left/Right ersetzen..
##erledigt

from Mengenzeiger4 import*
from math import *
import sys
sys.setrecursionlimit(20000)

screen= Screen()

pu()
goto(0,0)
shape("circle")
color("green")
showturtle()
pensize(5);shapesize(1)
pd()

def steigungZuWinkel(steigung):
        return atan(steigung)

##DEFINITIONSBEREICH DER KURVE
menge=np.arange(0,2*pi,0.01)


Mengenzeiger = Mengenzeiger(-200,-300,menge,screen, 222)

def updateSimulation(t):     
        goto(
                100*sin(2*menge[t]),
                100*sin(menge[t])
        
        ) 
        ##obige zwei Funktionen modellieren die Kurve
        
        
                
        



penup() ## Turtle bewegt sich ohne Stift zum Start
updateSimulation(0)
pendown() ## Turtle zeichnet Kurve












def moveleft():
        Mengenzeiger.moveLeft(True)
        updateSimulation(Mengenzeiger.t)
        
def moveright():
        Mengenzeiger.moveLeft(False)
        updateSimulation(Mengenzeiger.t)
        
screen.onkeypress(moveleft,"Left")
screen.onkeypress(moveright,"Right")
screen.listen()




mainloop()
