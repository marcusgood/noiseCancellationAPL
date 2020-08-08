import numpy as np
import matplotlib.pylab as plt
import padasip as pa
#from sin_data import sin_data

# these two function supplement your online measurment
def measure_x():
    time = np.arange(0, 30, .1); #generates 300 evenly spaced data points
    f = 1 #Hz
    a = 10 #Amplitude
    sin_data = a * np.sin(2 * np.pi * f * time)

    i = 0 #used to update position value for loop 
    for position in sin_data:  #loops through sin_data values to parse 3 different values each time
        position = i + 0
        value1 = sin_data[position]   #takes position 0, 3, 6, 9 etc
        value2 = sin_data[position + 1] #takes position 1, 4, 7, 10 etc
        value3 = sin_data[position + 2] #takes position 2, 5, 8, 11 etc
        i = i + 1
        x = np.array([value1, value2, value3])  #np.array to change from list to array values w/o commas
        #print (x)
    
        if i > 100: #controls number of times loops runs, and based on number of sin_data values, so does not parse over the maximum number of values 
            break
   
        return x
    
def measure_d(x):
    # meausure system output
    d = 2*x[0] + 1*x[1] - 1.5*x[2]
    return d
    
N = 100
log_d = np.zeros(N)
log_y = np.zeros(N)
filt = pa.filters.FilterLMS(3, mu=1.)
for k in range(N):
    # measure input
    x = measure_x()
    # predict new value
    y = filt.predict(x)
    print (y)
    # do the important stuff with prediction output
    pass    
    # measure output
    d = measure_d(x)
    # update filter
    filt.adapt(d, x)
    # log values
    log_d[k] = d
    log_y[k] = y
    
    
    
### show results
np.random.seed(52102)
plt.style.use('ggplot')    
plt.figure(figsize=(15,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("samples - k")
plt.plot(log_d,"b", label="d - target")
plt.plot(log_y,"g", label="y - output");plt.legend()
plt.subplot(212);plt.title("Filter error");plt.xlabel("samples - k")
plt.plot(10*np.log10((log_d-log_y)**2),"r", label="e - error [dB]")
plt.legend(); plt.tight_layout(); plt.show()