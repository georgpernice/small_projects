
from matplotlib import pyplot as plt
import math as m
import numpy as np
def f (x):
    a = np.array(
    [[1.0,0,1.0,4.0],
    [x,2.0,3.0,0.0],
    [0.0,0.0,2*x,1.0],
    [2.0,4.0,0.0,1.0]])


    return np.linalg.det(a)

x = np.linspace(-5,5,100)

# the function, which is y = x^2 here
y = np.linalg.det(np.matrix(
    [[1.0,0,1.0,4.0],
    [x,2.0,3.0,0.0],
    [0.0,0.0,2*x,1.0],
    [2.0,4.0,0.0,1.0]]))

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'r')

# show the plot
plt.show()
