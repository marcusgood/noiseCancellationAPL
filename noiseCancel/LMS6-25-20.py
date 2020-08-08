import numpy as np
import matplotlib.pylab as plt
import padasip as pa


#def desired_value(sin_wave):
#d =  2*sin_wave[position] + 1*sin_wave[position + 1] - 1.5*sin_wave[position + 2]
    #d = 0
    #return d


#def sin_data():
time = np.arange(0, 60, 0.01);

f = 1
a = 10

sin_data = a * np.sin(2 * np.pi * f * time)
      
LMSgraphing_data = []
desired = []
Errorgraphing_data = []
trials = 6000



i = 0
position = 0

for i in range(trials):

    value1 = sin_data[position]
    value2 = sin_data[position + 1]
    value3 = sin_data[position + 2]
    
    
    
    sin_wave = np.array([value1, value2, value3])
    
    #target = 0
    #target =  2*sin_data[position] + 1*sin_data[position + 1] - 1.5*sin_data[position + 2]
    target = -(2*sin_data[position] + 1*sin_data[position + 1] - 1.5*sin_data[position + 2])
    #print(target)
    desired.append(target)
    
    LMS = pa.filters.FilterLMS(3, mu = 0.013)
    prediction = LMS.predict(sin_wave)
    
    
    LMS.adapt(target, prediction)
    LMSgraphing_data.append(prediction)
    #print(d - prediction)
    position = position + 1
    
    
    error = prediction - target
    #print(error)
    
    Errorgraphing_data.append(error)
    
    if position == trials: #checks to make sure loop stays within given data, likely wont be needed with real time sound
        break
    if position + 1 == trials:
        break
    if position + 2 == trials:
        break
    
    
#d = desired_value(sin_wave)


    
plt.subplot(211);plt.title('Prediction')
plt.plot(desired, 'b', label = 'Filter Target')
plt.plot(LMSgraphing_data,"g", label="Output");
plt.legend()

plt.subplot(212);plt.title("Filter error");plt.xlabel("samples - k")
plt.plot(Errorgraphing_data, label = "error between prediction and target")
plt.legend(); plt.tight_layout(); plt.show()

