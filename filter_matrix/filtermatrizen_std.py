from turtle import*
speed(0)
screen = Screen()
screen.colormode(255)
from math import*
import numpy as np

DIM = 3

def floatToGrey(f): #Ziel: bilde (-10,10) ab auf Bereich 0,255 erzeugen
    res = 128 + int(1/20 * 255 * f)
    
    if(res>255):
        return(255,0,0) # out of range: rot!
    if(res<0):
        return(0,0,255) # out of negative range blau!
    return (res,res,res)
    
def showMat (mat,posx, posy):
    #AxA mat at posx and posy
    shape("square")
    res=20 # bildgröße
    
    for i in range(len(mat)):
        for j in range(len(mat)):
            color(floatToGrey(mat[j][i]))
            pu()
            goto(posx + i*res,posy - j*res)
            pd()
            stamp()
        
def printMat(mat):
    for i in range(len(mat)):
        outputline = ""
        for j in range(len(mat[0])):
            outputline += ("\t" +str(round(mat[i][j],2)))
        print(outputline+"\n")
    
def symmat_weightedSum(fMat, mat, pos):
    #annahme beide Matrizen 3x3
    
    sum = 0
    for i in (pos[0]-1, pos[0], pos[0]+1):
        for j in (pos[1]-1, pos[1], pos[1]+1):
            outside = False;
            a = fMat[i-pos[0]+1][j-pos[1]+1] # bei der filtermatrix
                                             #wandern wir im rein  bekannten gitter

            
            if((i<0)|(i>=3)):
                outside = True
            if((j<0)|(j>=3)):  # wenn i oder j ausserhalt der matrix mat2      
                outside = True
    
            if(outside): #dann nullsetzen der ben. werte der mat2
                b = 0
            else:
                b = mat[i][j]
            sum += a*b
    return sum
                       

def useFilter( mat , filmat ) :
    #gefilterte Matrix soll dieselbe Dimension haben, d.h
    #wir müssen in der weightedSum funktion einstellen dass er nur vorhandene
    #zahlen verwendet
    
    resMat = 
    for i in range(len(mat)):
        for j in range(len(mat)):
            resMat[i][j] = symmat_weightedSum(filmat, mat,(i,j))
                                         
    return resMat

#Testkaninchen initialisieren und zeigen..
matrix = ((-1,-2,0),
          (1,-6,1),
          (1,1,2))
matrix2 = ((1,1,1,1,1),(0,0,0,1,1),(2,2,2,2,-4),(-3,3,2,1,2),(-3,9,2,1,2))
showMat(matrix2,10,10)
#Filter initialisieren 
f_gauss = [[1/16,2/16,1/16],[2/16,4/16,2],[1/16,2/16,1/16]]
f_rechteck = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

showMat(useFilter(matrix, f_rechteck),100,100)
showMat(useFilter(matrix, f_gauss),-100,100)
#numpy anwenden weil numpymatrix[0,0] gibt das element links oben zurück
# außerdem einfachere definition
