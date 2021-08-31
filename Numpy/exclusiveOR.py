"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 13:08:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
will return the sorted, unique values that are in only one (not both) of the input arrays.
"""
import numpy as np

arr1=np.array([0,10,20,40,60,80])
arr2=np.array([10,30,40,50,70])
print(np.setdiff1d(arr1,arr2))
print(np.setdiff1d(arr2,arr1))