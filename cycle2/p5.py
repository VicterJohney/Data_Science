#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:40:50 2021

@author: sjcet
"""

#5. Create an 1D array with arange containing first 15 even numbers as elements

#a. Elements from index 2 to 8 with step 2(also demonstrate the same using slice function)
#b. Last 3 elements of the array using negative index
#c. Alternate elements of the array
#d. Display the last 3 alternate elements


import numpy as np

array_1d=np.array([0,2,4,6,8,10,12,14,16,18,20,22,24,26,28])
print("Elements from index 2 to 8 with step 2",array_1d[2:8:2])
print("Last 3 elements of the array using negative index",array_1d[-3:-1])
print("Alternate elements of the array",array_1d[::2])
print("Display the last 3 alternate elements",array_1d[-3:-1:2])