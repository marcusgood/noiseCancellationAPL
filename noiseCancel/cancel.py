import numpy as np
import matplotlib.pylab as plt
import padasip as pa
import math as mat


time = np.arange(0, 25.02, 0.01);

f = 1.0
a = 1.0

phase = (2 * np.pi * f * time)

inputSignal = a * np.sin(phase)  #Test ideal sound wave


plt.figure(1)
plt.plot(time, inputSignal)
plt.title('Input Signal')
plt.xlabel('Time(sec)')
plt.show()

desiredSignal = -inputSignal #Goal to be generated

plt.figure(2)
plt.plot(time, desiredSignal)
plt.title('Desired Signal')
plt.xlabel('Time(sec)')
plt.show()

v = 3 #number of variables in sound wave that need to be adapted to (Amplitude, phase, up/down, frequency)
mu = 0.013 #learning rate
w = np.array([0,0,0])

error = []
output = []
weightValues = []


for n in range(v, len(inputSignal)):
    d = desiredSignal[n]
    x = inputSignal[n:n-v+0:-1] # inputs from 15-0, and shifts by one data point each trial (filter must get data from highest to lowest index)
    y = np.dot(w,x) #multipies w by x
    e = d - y
    w = w + mu * e * x
    #y,e,w = f.adapt(d, x)
    output.append(y)
    error.append(e)
    weightValues.append(w)

plt.figure(3)
plt.plot(time, error)
plt.title('Error over Time')
plt.xlabel('Time(sec)')
plt.show()

plt.figure(4)
plt.plot(time, output)
plt.title('Output over Time')
plt.xlabel('Time(sec)')
plt.show()

plt.figure(5)
plt.plot(time, weightValues)
plt.title('Weight Values over Time')
plt.xlabel('Time(sec)')
plt.show()