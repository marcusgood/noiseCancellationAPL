import numpy as np
import matplotlib.pylab as plt
import padasip as pa


def sin_data():
    time = np.arange(0, 5, 0.1);

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
        value3 = sin_data[position +2]


        i = i + 1
        sin_wave = np.array([value1, value2, value3])
        return sin_wave

        if i > 300:
            break

        return sin_wave

def desired_value(sin_wave):
    d =  2*sin_wave[0] + 1*sin_wave[1] - 1.5*sin_wave[2]

    return d

LMSgraphing_data = []



trials = 50
i = 0

sin_wave = sin_data()
for i in range(trials):

    LMS = pa.filters.FilterNLMS(3, mu = 0.017)

    prediction = LMS.predict(sin_wave)

    pass
    d = desired_value(sin_wave)
    LMSgraphing_data.append(prediction)
    LMS.adapt(d, prediction)

plt.plot(LMSgraphing_data)
plt.title('LMS Sin Function')
plt.xlabel('# of Trials')
plt.ylabel('LMS Sin Function')
plt.axhline(y=0, color='black')
plt.show()
#print(LMSgraphing_data)
