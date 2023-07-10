import math
#thomas algorithmus 
#define matrix diagonals
N = 5 #Length of main diagonal

a = [0,1,1,1,1]         # die '0' am Anfang weil a bei a2 beginnt
b = [-2,-2,-2,-2,-2]
c = [1,1,1,1,0]         # c endet bei c4

d = [-1,-1,-1,-1,-1]    #define righthandside

u = [0] * N             #empty velocity vector
e = [0] * N             #empty e
f = [0] * N             #empty f


# -2 	 1	   0	0	 0		    -1
#  1	-2	   1	0    0		    -1
#  0	 1    -2    1 	 0  	    -1
#  0	 0	   1   -2    1  	    -1
#  0	 0	   0    1   -2 	        -1


#Koeffizienten Startbedingung:
e[0] = c[0]/b[0] # da u1 = 0 b1 beliebig
f[0] = d[0]/b[0]

for i in range(N-1):
    e[i+1] = c[i] / (a[i] * e[i] +b[i])
    f[i+1] = (d[i] - a[i]*f[i]) / (a[i]*e[i] + b[i])
    print("i="+str(i)+"=> " +
     "e["+str(i+1)+"] = "+ str(round(e[i+1],2)) + "\t" + 
     "f["+str(i+1)+"] = "+ str(round(f[i+1],2)))

print()
u[4] = 1

for i in range(N-1, 1, -1): #Rückwärtseinsetzen
    
    u[i-1] = e[i] * u[i] + f[i]
    print("i-1="+str(i-1)+"=> " + "\t" +
     "u["+str(i-1)+"] = "+ str(round(u[i-1],2)))