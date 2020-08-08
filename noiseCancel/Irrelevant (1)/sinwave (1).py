import numpy as np
import matplotlib.pyplot as plot


def sin_data():
    time = np.arange(0, 30, 0.1); #generates data points
    #print (time)

    f = 1 #Hz
    a = 10 #amplitude

    sin_data = a * np.sin(2 * np.pi * f * time)
    print (sin_data)

    with open('sincurvedata.txt', 'w') as filehandle:    #writes data to sincurvedata.txt
        filehandle.writelines("%s\n" % item for item in sin_data)
        

    #data_input = sin_data[0:3:1]            #loops to take two data values from sin_data
    #print (data_input)
    print(sin_data)

    

    plot.plot(time, sin_data)                         #matplotlib graph 
    plot.title('Sine Wave Data')
    plot.xlabel('Time (Seconds)')
    plot.ylabel('Sin Function Value ')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='black')
    plot.show()

 

sin_data()


