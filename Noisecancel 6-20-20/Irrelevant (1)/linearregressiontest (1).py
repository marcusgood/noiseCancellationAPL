# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:50:20 2019

@author: goodm1
"""
import numpy as np
#import matplotlib.pyplot as plt 

xValues = (1, 2, 4) #will become sensor inputs
yValues = (2, 1, 3)

z = len(xValues)

#Calc values for linear regression slope
meanX = np.mean(xValues)
    
meanY = np.mean(yValues)

meanXSq = meanX * meanX 

print("meanX" ,meanX, "meanY" ,meanY, "meanXSq" ,meanXSq,)

#plug into slope formula

slope = ((meanX * meanY) - (16/3))/((meanX * meanX) - (7))
print('Slope' ,slope,)

#find y-int (b value) for linear regression equation

yInt = (meanY) - ((slope) * (meanX))

print('yInt',yInt,)

#calculate the r squared value 

#graph points and linear regression formula (with r squared value)
