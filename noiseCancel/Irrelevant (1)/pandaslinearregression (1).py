# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 14:50:20 2019

@author: goodm1
"""
import numpy as np
#import matplotlib.pyplot as plt 

xValues = (1, 2, 4)
yValues = (2, 1, 3)

meanX = np.mean(xValues)
    
meanY = np.mean(yValues)

meanXY = meanX * meanY

meanXSq = meanX * meanX 

print(meanX, meanY, meanXY, meanXSq)