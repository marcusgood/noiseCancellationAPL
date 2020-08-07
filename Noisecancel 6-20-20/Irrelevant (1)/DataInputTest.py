import numpy as np
#data_values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


#print (value1)


time = np.arange(0, 50, .1); #generates 500 evenly spaced data points
f = 1 #Hz
a = 10 #Amplitude
sin_data = a * np.sin(2 * np.pi * f * time)

i = 0
for position in sin_data:  
    position = i + 0
    value1 = sin_data[position]   #equals the number at the position defined by the function
    value2 = sin_data[position + 1]
    i = i + 2
    x = [value1, value2]
    if i > 250:  #needs to be adjusted depending on amount of data generated, and how many times it needs to be parsed
        break
    print (x)
    

   
    
    
    
    
    