from math import*
from time import*

        

def potenzAnsatz(x):
    return 4*pow(x,4)+2*pow(x,3)-3*pow(x,2) + 7

def hornerAnsatz(x):
    a=[4,2,-3,0,7]
    b=0
    for i in a:
        
        if (i==a[0]):
            b=a[0]
        else:
            b=b*x+i

    return b


starttime=time()
print ("Potenz:\n", potenzAnsatz(10000000000000000000000000))
time2 = time()
print("Length: ", time2-starttime)
print("Horner:\n", hornerAnsatz( 10000000000000000000000000))
time3=time()
print("LengthHorner: ", time3-time2)

