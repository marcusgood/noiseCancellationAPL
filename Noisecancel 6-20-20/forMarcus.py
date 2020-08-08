# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:37:25 2020

@author: samsuj1
"""

import numpy as np
import matplotlib.pylab as plt
import padasip as pa
import math as mat

plt.close('all')

t= np.arange(0, 25, 0.01)
#print(time)
f = 1.0 #frequency
A = 1.0 #Amplitude
phase = (2*mat.pi*f*t) #in radians
#print(phase)

desiredSignal = -1.0*np.cos(phase)
#print(desiredSignal)

plt.figure(1)
plt.plot(t, desiredSignal)
plt.title('Desired Signal')
plt.xlabel('Time(sec)')
plt.show()
inputSignal = - desiredSignal

M =15  #filter length ???
f = pa.filters.FilterLMS(M, mu=0.1)
yy =[]
ee =[]
ww =[]
w = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
mu = .1
#LMS algorithm
for n in range(M,len(inputSignal)):
    d = desiredSignal[n]
    x = inputSignal[n:n-M+0:-1]
    y = np.dot(w,x)
    e = d - y
    w = w + mu * e * x
    #y,e,w = f.adapt(d, x)
    yy.append(y)
    ee.append(e)
    ww.append(w)

plt.figure(2)
plt.plot(t[14:2500-1:1], ee)
plt.title('error')
plt.xlabel('Time(sec)')
plt.show()

plt.figure(3)
plt.plot(t[14:2500-1:1], yy)
plt.title('Estimated Signal')
plt.xlabel('Time(sec)')
plt.show()
