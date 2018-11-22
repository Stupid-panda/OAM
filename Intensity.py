# -*- coding: utf-8 -*-
"""
Created on Fri May  4 08:59:24 2018

@author: xu765
"""
#from scipy import special as S
from scipy.special import assoc_laguerre
import numpy as np
from numpy import pi
from matplotlib import pyplot as plt 

Lamda=400e-9
k=2*pi/Lamda
p=1
l=2
w0=0.3

r=np.arange(0,1,0.005)
theta=np.arange(0,8*pi,0.01)
R,Theta=np.meshgrid(r,theta)
x = R*np.cos(Theta)
y = R*np.sin(Theta)
#Ie=(((2**0.5)*R)**(2*l))*np.exp(-2*R**2)*(S.assoc_laguerre(2*R**2,p,l))**2
E=((2**0.5*R/w0)**l)*np.exp(-1*R**2/w0**2)*assoc_laguerre(2*R**2/w0**2,p,l)*np.exp(complex(0-1j)*l*Theta)
Ie=(abs(E))**2  #at z=0

plt.pcolormesh(x,y,Ie)
plt.axis('off')
plt.show()
#L=S.eval_genlaguerre(1, 1, x)