"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 15:33:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program compare two arrays using numpy.
"""
import numpy as np 

arr1=np.array([1,2])
arr2=np.array([4,5])

print(np.greater(arr1,arr2))
print(np.less(arr1,arr2))
print(np.greater_equal(arr2,arr1))
print(np.less_equal(arr2,arr1))