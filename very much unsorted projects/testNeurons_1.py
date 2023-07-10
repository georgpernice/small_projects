# Ziel ist ein Neuronales Netz dass  auf einer 2x2 Matrix erkennt,
# wenn ein Muster vorliegt in dem sich die Einsen nicht
# gegenseitig berühren sonder höchstens diagonal
from random import*


iMat_2x2= [1,0,1,0]

#Define weights

weights = [0,0,1,0] #init weights
#Define border for activation
BORDER=2

##-----------------------------
## Neuron put functions
##-----------------------------
def matPrint(mat):
    print( mat[0] , mat[1])
    print( mat[2] , mat[ 3])

def activation_N(parameters):
    res = 0
    for i in range(4):
        res += weights[i] * parameters[i]
    return res
def loss (parameters):
    return (activation_N(parameters) - BORDER)
def outputN(parameters):
    return loss(parameters)>0


def trainN(data):
    global weights
    for i in range (len(data)):
            matrix = data[i][0]
            diagonal_bool = data[i][1]

            ##addiere einen teil
            while (outputN(matrix) != diagonal_bool):
                for w in weights:
                    w=w+random() 
                    
            
                        
                        
    
     
            
            

            

                
def stats():
    print("-- Weights -- ")
    matPrint(weights)
    print("-- -- -- -- --")

stats()
trainingData = (
([0,1,0,0],True),
([1,1,0,0],True),
([0,1,1,0],False),
([0,1,0,1],False),
([0,1,1,1],False)

            )
trainN(trainingData)
stats()
