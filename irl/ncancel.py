import numpy as np
import matplotlib.pylab as plt


time = np.arange(0, 25.0, 0.01);

f = 1.0  #certain changes of these lead to instability, due to lack of trials?
a = 1.0

inputSignal = a * np.sin(2 * np.pi * f * time)  #Test ideal sound wave

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

deltas = 4 #number of variables in sound wave that need to be adapted to (Amplitude, phase, up/down, frequency)
mu = 0.013 #learning rate
w = np.array([0,0,0,0])

error = []
output = []
weightValues = []


def ncancel(soundInput):

    for trials in range(deltas, len(inputSignal)):
        d = desiredSignal[trials]
        x = inputSignal[trials:trials-deltas+0:-1] # inputs from 4-0, and shifts by one data point each trial (filter must get data from highest to lowest index)
        y = np.dot(w,x) #multipies w by x
        e = d - y
        w = w + mu * e * x
        #y,e,w = f.adapt(d, x)
        output.append(y)
        error.append(e)
        weightValues.append(w)

    plt.figure(3)
    plt.plot(time[3:2500-1:1], error)
    plt.title('Error over Time')
    plt.xlabel('Time(sec)')
    plt.show()

    plt.figure(4)
    plt.plot(time[3:2500-1:1], output)
    plt.title('Output over Time')
    plt.xlabel('Time(sec)')
    plt.show()

    plt.figure(5)
    plt.plot(time[3:2500-1:1], weightValues)
    plt.title('Weight Values over Time')
    plt.xlabel('Time(sec)')
    plt.show()
