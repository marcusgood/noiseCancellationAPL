import numpy as np
import matplotlib.pylab as plt
import padasip as pa


def sin_data():
    time = np.arange(0, 200, 0.1);

    f = 1
    a = 10

    sin_data = a * np.sin(2 * np.pi * f * time)

    i = 0
    for position in sin_data:  #loops through sin_data values to parse 3 "stacked" values
        position = i
        #value1 = sin_data[position]
        #value2 = sin_data[position + 1]
        #value3 = sin_data[position + 2]
        value1 = sin_data[position]
        value2 = sin_data[position +1]
        value3 = sin_data[position +1]
        value4 = sin_data[position+1]


        i = i + 1
        sin_wave = np.array([value1, value2, value3, value4])
        return sin_wave



N = 500
x = sin_data()
print(x)
v = np.random.normal(0, 1, N) * 0.1
d = 2*x[:,0] + 0.1*x[:,1] - 4*x[:,2] + 0.5*x[:,3] + v

# identification
f = pa.filters.FilterNLMS(mu=0.5, n=4)
y, e, w = f.run(d, x)

# show results
plt.figure(figsize=(12.5,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("Number of iteration [-]")
plt.plot(d,"b", label="d - target")
plt.plot(y,"g", label="y - output")
plt.xlim(0, N)
plt.legend()

plt.subplot(212); plt.title("Filter error"); plt.xlabel("Number of iteration [-]")
plt.plot(pa.misc.logSE(e),"r", label="Squared error [dB]");plt.legend()
plt.xlim(0, N)
plt.tight_layout()
plt.show()
print("And the resulting coefficients are: {}".format(w[-1]))
