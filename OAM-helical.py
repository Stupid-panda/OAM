
import numpy as np
from numpy import pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

Lamda=400e-9
k=2*pi/Lamda
z=[]
l=3
fai=2*pi/l
n=0
while n<l:
    theta=np.arange(0+fai,8*pi/l+fai,0.01)
    r=np.arange(0,1,0.005)
    R,Theta=np.meshgrid(r,theta)
    temp=l*(Theta-fai*np.ones((R.shape[0],R.shape[1])))/k
    fai=2*pi/l+fai
    z.append(temp)
    x = R*np.cos(Theta)
    y = R*np.sin(Theta)
    ax.plot_surface(z[n],x,y,rstride=1, cstride=1, cmap='rainbow')
    n=n+1
plt.axis('off')
plt.show()