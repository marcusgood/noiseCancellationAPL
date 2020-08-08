import numpy as np
import matplotlib.pylab as plt
import padasip as pa 

# these two function supplement your online measurment
def measure_x(): 
    # it produces input vector of size 3
    
    F = 50         # No. of cycles per second, 
    T = 0.02        # Time period,
    Fs = 50.e3        # No. of samples per second, Fs = 50 kHz
    Ts = 1./Fs        # Sampling interval, Ts = 20 us
    N = int(T/Ts)     # No. of samples for 2 ms, N = 100

    t = np.linspace(0, T, N)
    x = np.sin(2*np.pi*F*t)

    plt.plot(t, y)
    plt.xlabel('Time (s)')
    plt.ylabel('Sound wave Value')
    plt.show()

    print(x) #gives the 3 values through loop's 100 rev.
    return x
    
def measure_d(x):
    # measure system output
    d = 0   #Why do they want this output
    return d
    
N = 100  #For loop N times
log_d = np.zeros(N) #np.zeros(N) gives array of zeros
#print(log_d) 
log_y = np.zeros(N) #np.zeros(N) gives array of zeros
#print(log_y)
filt = pa.filters.FilterLMS(3, mu=0.7, w='random') #defines filter as LMS, with 3 coefficent and mew(learning step) of 0.7
for k in range(N):
    # measure input
    x = measure_x()
    # predict new value
    y = filt.predict(x) #passes random 1D 3 value input into filter
    
    filter_predict = y
    
    #print(filter_predict)
    # do the important stuff with prediction output
    pass    #waits some time for prediction
    # measure output
    d = measure_d(x) #predicted outputed to 'd' and then compared to the x of the desired before
    
    desired_measure = d
    #print(desired_measure)
    # update filter
    filt.adapt(d, x) #Then adapts the filter to the error between the desired and predicted using the previously found inputs from the filter 
    # log values
    log_d[k] = d #multiplies zeros of N time loops by the number of times looped and sets that equal to the desired
    log_y[k] = y #multiplies zeros of N time loops by the number of times looped and sets that equal to the prediction of the filter
    
### show results
plt.figure(figsize=(15,9))
plt.subplot(211);plt.title("Adaptation");plt.xlabel("samples - k")
plt.plot(log_d,"b", label="d - target")
plt.plot(log_y,"g", label="y - output");plt.legend()
plt.subplot(212);plt.title("Filter error");plt.xlabel("samples - k")
plt.plot(10*np.log10((log_d-log_y)**2),"r", label="e - error [dB]")
plt.legend(); plt.tight_layout(); plt.show()