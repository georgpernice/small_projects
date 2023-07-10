# Programm splitting circle with radius r in polygons of m edges
# Middlepoint M
# Polygonedge P

# imports
import math
from turtle import*
penup()
tracer(False)

def alpha(m):
    return 2*pi/m
def M(r):
    # middlepoint M = origin
    m1 = 0
    m2 = 0
    return (m1,m2)

def P(r,m):
    # Polygon edge P
    #p1 = r*(1 + (math.cos(alpha(m)) + 1) * math.cos(alpha(m)))
    p1 = r * math.tan(pi / EDGES)
    p2 = r*(-1)
    return (p1,p2)

def rotate_xy_around_origin(x,y,alpha):
    # alpha in radian
    # works with 2D-Rotationsmatrix
    x_ = math.cos(alpha) * x + math.sin(alpha) * y 
    y_ = -math.sin(alpha)* x + math.cos(alpha) * y
    return (x_,y_)

def P_edge_n(r,m,n):
    # draw P_n for edge n
    x,y = P(r,m)
    x_,y_ = rotate_xy_around_origin(x,y,alpha(m))
    return (x_,y_)

# constants
pi = 3.1415926
R = 100
EDGES = 9



# draw middlepoint = origin
goto(0,0)
write("M = Origin")
dot(10)

#draw blue circle around origin with radius E
goto(0,-R)
pendown()
color("blue")
circle(R)
color("black")
penup()



# draw first edge P (n=1)
goto(P(R,EDGES))
dot(10)

# save edges in list
x,y = P(R,EDGES)
edges_list = []
for i in range(EDGES):
    edges_list.append(
        (rotate_xy_around_origin(x,y, alpha(EDGES) * (i+1)))
        )
# add the rest of the edges by rotating P around origin
color("red")
for e in edges_list:
    goto(e)
    dot(10)

# draw Q
x = math.sin(alpha(EDGES))
y = -math.cos(alpha(EDGES))
goto(x*R,y*R )
color("orange")
dot(10)
# draw Q's Tangente
t = 1000
pd()
goto(x*R + t * math.cos(alpha(EDGES)) ,y*R + t * math.sin(alpha(EDGES)))





