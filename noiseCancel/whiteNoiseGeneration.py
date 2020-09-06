import numpy as np
import matplotlib.pylab as plt

time = np.arange(0, 25.0, 0.1);
time2 = np.arange(0, 25.0, 1);
a = 1.0
f = 1.0

inputSignal = a * np.sin(2 * np.pi * f * time)

whiteNoise = np.random.normal(0, 1, 25)

noNoise = -(whiteNoise)

plt.figure(1)
plt.plot(time, inputSignal, whiteNoise)
plt.title('Sound vs Time')
plt.xlabel('Time')
plt.ylabel('Sound Input')
plt.show()


plt.figure(2)
plt.plot(time2, whiteNoise, noNoise)
plt.title('Cancel Goal')
plt.xlabel('Time')
plt.ylabel('Sound Input')
plt.show()
