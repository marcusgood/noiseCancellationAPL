import numpy as np
import matplotlib.pyplot as plot


def sin_data():
    time = np.arange(0, 60, 0.01); #generates 500 data points

    f = 1 #Hz
    a = 10 #amplitude

    sin_data = -(a * np.sin(2 * np.pi * f * time))
    print (sin_data)


    #with open('sincurvedata.txt', 'w') as filehandle:    #writes data to sincurvedata.txt, to be passed into LMS filter
        #filehandle.writelines("%s\n" % item for item in sin_data)
    #data_input = sin_data[0:4:1]            #loops to take two data values from sin_data
    #print (data_input)




    plot.plot(time, sin_data)                         #matplotlib graph
    plot.title('Sine Wave Data')
    plot.xlabel('Time (Seconds)')
    plot.ylabel('Sin Function Value ')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='black')
    plot.show()

    return sin_data

sin_data()
