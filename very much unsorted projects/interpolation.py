from turtle import*
##Programm läuft nur für Messwertzahl N = 3 momentan zuverlässig
##-> Demnächst Kapazität erhöhen durch überarbeiten von interpolate
##-> Dazu eventuell Trainingsdaten erforderlich



##FACT = 100
##screen = Screen()
##pointy = Turtle()
##pointy.shape("circle")
##pointy.turtlesize(0.3,0.3,1)
##pointy.pu()
##drawer = Turtle()
##drawer.ht()
##
##speed(0)
##tracer(False)
##
##import matplotlib.pyplot as plt
##import numpy as np
##
### Data for plotting
##t = np.arange(0.0, 300.0, 1) #xwerte



#values = [(0,0)]
#values= [(0,0),(20,40),(50,100),(90,180)]
#values = [(0,2),(2,0),(4,1),(5,-3),(7,8)]
values = [(1,200),(2,30),(3,5),(4,44),(5,11),(6,12),(10,-4),(12,0)]
a = [] #vorläufig init.
n = len(values) -1 #polynomgrad

def add(x,y):
    global values
    global n 
    if (x*FACT > values[-1][0]): # letztes element der liste ist ein tupel (x,y)
        values.append((x*FACT,y))
        n = len(values) -1 
        pointy.goto(x,y)
        pointy.stamp()
    else:
        pass



def dd(a,b,iErste,iLetzte):
    return (a-b) / (values[iErste][0] - values[iLetzte][0])












   
def interpolate():
    
    global a
    global values
    a.append(values[0][1])#erster Koeffizient ist erster y-Wert
    
    #bilde hilfsarray dd2 mit zweistelligen dd
    dd2 = []
    for i in range(n):##KLAPPT
        dd2.append(dd(values[i+1][1],values[i][1], i+1,i))
        

    for k in range(n):#vollständige dd mit kommaeins bestimmen für alle D454321,D4321 usw.
                        # -1 wegen python indizes
        
        zw = dd2[k]#greift auf 54 zu
        print("HEY zw startet als ", zw, "!")
        print("#Beginne innere Schleife", "( k = ", k, ")")
        for j in range(k):
            
            i=k-j#i läuft rückwärts
            print("Index i: ", i )
           
            print("Verkette zw:",zw, " mit dd2[i-1]: ", dd2[i-1])
            zw = dd(zw,dd2[i-1],k+1,i-1) # achtung äußere indizes
            
        a.append(zw)
    
    






        
    

def polynomString(x): #FERTIG
    summe = 0
    faktor = 1
    faktorString = ""
    summeString = "polynom(x) = \t"
    
    for i in range(n+1): # aussummieren der koeffizierten
        
        if(i==0):
            pass
            
        else:
            faktor = faktor * (x-values[i-1][0])
            faktorString = faktorString  + "(x - " + str(values[i-1][0]) + ")"  
        
        summe = summe + a[i]*faktor 
        summeString = summeString + "+" + str(a[i])  + faktorString + "\n\t\t"
        
    print(summeString)    
        
        
    return summe
def polynom(x): #FERTIG
    summe = 0
    faktor = 1
    faktorString = ""
    summeString = "polynom(x) = \t"
    
    for i in range(n+1): # aussummieren der koeffizierten
        
        if(i==0):
            pass
            
        else:
            faktor = faktor * (x-values[i-1][0])
            faktorString = faktorString  + "(x - " + str(values[i-1][0]) + ")"  
        
        summe = summe + a[i]*faktor 
        summeString = summeString + "+" + str(a[i])  + faktorString + "\n\t\t"
        
      
        
        
    return summe

def drawLine():
    tracer(True)
    goto(0,0)
    for i in range(100):
        x= drawer.xcor()*FACT
        y= drawer.ycor()*FACT
        pol= polynom(x)*FACT
        
       

        drawer.goto(x+1,y+pol+1)
       
    
    

def drawInterpolation(): #überladen wegen onkeypress
    print("Koeffizienten vor Interpolation: ", a)
    print("Values vor Interpolation: ", values)
    interpolate()
    
    print("Koeffizienten dannach: ", a)
    print("Values nach Interpolation: ", values)
    
    #drawLine()
##
##    #Plotten
##    s = polynom(t)
##    
##    fig, ax = plt.subplots()
##    fig2, ax2 = plt.subplots()
##    ax.plot(t, s)
##    xVals=[]
##    yVals=[]
##    for val in values:
##        xVals.append(val[0])
##        yVals.append(val[1])
##    ax2.plot(xVals,yVals)
##
##    #ax.set(xlabel='time (s)', ylabel='voltage (mV)',
##           #title='About as simple as it gets, folks')
##    #ax.grid()
##    ax2.grid()
##    
##    plt.show()
    print("The computed interpolation polynom is:")
    polynomString(0)
    print("\n Checking the righteousness of our computation.. \n")
    for point in values:
        print("polynom(",point[0],")","=",polynom(point[0]), "while Point ", point, " should be in the polynom")
        pass
    
    
#onscreenclick(add)
#onkeypress(
drawInterpolation()
#,"Return")
#screen.listen()




