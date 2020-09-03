import padasip as pa 
import numpy as np
import matplotlib.pylab as plt



def main():






def sin_data():
    time = np.arange(0, 5, 0.001); #generates data points
    f = 300 #Hz
    a = 10 #amplitude

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


        i = i + 1
        sin_wave = np.array([value1, value2, value3])


        return sin_wave




def desired_value(sin_data):

	d = 0 



LMSgraph = []
time = np.arange(0, 5, 0.001); 




def LMS_prediction(sin_data):
	LMS = pa.filters.FilterLMS(3, mu= 0.013)

	prediction = LMS.predict(sin_data)

	LMSgraph.append(prediction)





plt.plot(time, LMSgraph)
plt.title('LMS Sin Function')
plt.xlabel('Time')
plt.ylabel('Predicted LMS Sin Function')
plt.axhline(y=0, color='black')
plt.show()