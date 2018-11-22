# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:48:16 2018

@author: xu765
"""

import numpy as np
from numpy import pi
from matplotlib import pyplot as plt
from scipy.special import assoc_laguerre

Lamda=400e-9
k=2*pi/Lamda
l=5
p=0

theta=np.arange(0,2*pi,0.01)
r=np.arange(0,3,0.05)
R,Theta=np.meshgrid(r,theta)

x = R*np.cos(Theta)
y = R*np.sin(Theta)
E=np.exp(-1*R**2)*(((2**0.5)*R)**l)*np.exp(complex(0-1j)*l*Theta)*assoc_laguerre(2*R**2,p,l)
fai=np.angle(E)

plt.pcolor(x,y,fai)
plt.axis('off')
plt.show()


#fai=(2*p+l+1)*math.atan(z)
#import math