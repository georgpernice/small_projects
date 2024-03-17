from turtle import*
import numpy as np
class Mengenzeiger(Turtle):

    
    def __init__(self, x, y, menget, scr, w):
        Turtle.__init__(self)
        
        self.homeX=x
        self.homeY=y
        self.width=w
        self.shape("triangle")
        self.shapesize(1)
        self.penup()
        self.speed(6)
        self.goto(self.homeX,self.homeY)
        self.anzahl = len(menget)
        self.t=0
        self.x = x
        self.pendown()
        self.goto(self.homeX + self.width, self.homeY)
        self.write(round(menget[self.anzahl-1],2),font=("Arial",18,"normal"))
        self.goto(self.homeX + 0.5*self.width, self.homeY)
        self.write(round(   menget[int(   self.anzahl//2  )   ],2)   ,font=("Arial",18,"normal"))
        self.goto(self.homeX,self.homeY)
        self.write(round(menget[0],2), font=("Arial",18,"normal"))
        
    def moveLeft(self, Left):
##        print("x :",x)
        #print((x>self.homeX+self.width),(x<self.homeX-10))
        
        if(self.x<self.homeX+self.width-1):
            if(Left==False):
                self.x =self.x + 1
                # +-10 wurde entfernt
        if(self.x>self.homeX):
            if(Left==True):
                self.x = self.x - 1
                
        
            
        self.goto(self.x,self.homeY)
        self.t=int(round(((self.x-self.homeX)/self.width)*self.anzahl))
        #print(self.t)
   
