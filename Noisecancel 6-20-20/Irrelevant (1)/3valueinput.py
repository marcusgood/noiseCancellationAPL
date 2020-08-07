import numpy as np


time = np.arange(0, 60, .1); #generates 500 evenly spaced data points
f = 1 #Hz
a = 10 #Amplitude
sin_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]             #a * np.sin(2 * np.pi * f * time)



i = 0
for position in sin_data:  #why does this position equal 2
    position = i + 0
    value1 = sin_data[position]   #equals the number at the position defined by the function
    value2 = sin_data[position + 1]
    value3 = sin_data[position + 2]
    i = i + 1
    x =np.array([value1, value2, value3])
    
    if i > 200:
        break
    print (x)