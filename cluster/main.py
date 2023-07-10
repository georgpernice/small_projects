
import numpy as np
import matplotlib.pyplot as plt
import math as m



datatupels=[

[83.80,2.30],#daten dieselpreis vs brotpreis von 2002 bis 2020
[88.80,2.50],
[94.20,3.10],
[106.70,3.20],
[111.80,3.25],
[117,3.25],
[133.50,3.35],
[108.50,3.40],
[122.40,3.70],
[141.90,3.60],
[148.90,3.65],
[142.80,3.70],
[135,3.90],
[117.10,4.05],
[107.20,4.25],
[115.60,4.34],
[128.90,4.55],
[126.70,4.62],
[112.40,4.65]

]




plt.scatter(*zip(*datatupels))
plt.show()
def distance(dt1,dt2):
    return m.sqrt(pow(dt1[0]-dt2[0],2)+pow(dt1[1]-dt2[1],2))
def findSmallestDistanceClusterIndex(dt, clustercenters):
    if distance(dt,clustercenters[0]) < distance(dt,clustercenters[1]):#aname dass 2 cluster 
        return 0
    else:
        return 1

def centerOfDatatupels(datatupels):
    component_0 = 0
    component_1 = 0
    for dt in datatupels:
        component_0 += dt[0] 
        component_1 += dt[1]
    return (component_0 / float(len(datatupels)) , component_1 / float(len(datatupels)))

clustercenters = [[100,3.5],[80,6]]#aname dass 2 cluster 

for k in range(4):
    datatupelsCluster0 = []
    datatupelsCluster1 = []
    #ZUWEISUNG
    for dt in datatupels:
        index = findSmallestDistanceClusterIndex(dt,clustercenters)
        if(index==0):
            datatupelsCluster0.append(dt)
        else: #aname 2 cluster
            datatupelsCluster1.append(dt)
        
    #CLUSTERZURECHTRÜCKEN
    if(len(datatupelsCluster0)>0):
        clustercenters[0] = centerOfDatatupels(datatupelsCluster0)
        print(datatupelsCluster0)
    if(len(datatupelsCluster1)>0):
        clustercenters[1] = centerOfDatatupels(datatupelsCluster1)
        print(datatupelsCluster1)
         

#plt.plot(datatupels , "ob" )
plt.plot(*zip(*clustercenters), color = "g", marker = "o")
plt.scatter(*zip(*datatupels), color = "b", marker = "+")
plt.show()
print(clustercenters)