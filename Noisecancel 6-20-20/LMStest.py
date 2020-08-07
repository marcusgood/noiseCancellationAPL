import numpy as np
import matplotlib.pylab as plt
import padasip as pa


def sin_data():
    time = np.arange(0, 10, .1); #generates 300 evenly spaced data points
    f = 1 #Hz
    a = 10 #Amplitude
    sin_data = a * np.sin(2 * np.pi * f * time)
    #print(sin_data)
    i = 0
    
    for position in sin_data: 
        position = i + 0
        value1 = sin_data[position]   
        value2 = sin_data[position + 1] 
        value3 = sin_data[position + 2] 
        i = i + 1
        data_input = np.array([value1, value2, value3])#np.array to change from list to array values w/o commas
        if i > 100: 
            break
        return data_input
    
def desired_output():
    d = 0 #Want input wave and output wave to cancel
    return d
    
number_reps = 100
LMS_data = [] #stores all # of reps data in array for plt
sin_data()



for i in range(number_reps):
    
    x = data_input        
    LMS = pa.filters.FilterLMS(3, mu=0.1)
    output = LMS.predict(x)
    
    
    LMS.adapt(0, x) #adapts weights of filter based on desired output
    
    #print(np.arange(output))
    LMS_data.append(output)
    
        
plt.plot(LMS_data)                         
plt.title('LMS Sin Function')
plt.xlabel('# of Reps')
plt.ylabel('LMS Sin Function')
plt.grid(True, which='both')
plt.axhline(y=0, color='black')

plt.show()
    
    
    
    
    
    
#Correct step size, number of reps to get accurate output
    
#How to determine stepsize/reps, number of input variables (amplitude, frequency, shift L/R (eventually) )
#How to determine these componets from acutal sound waves
    