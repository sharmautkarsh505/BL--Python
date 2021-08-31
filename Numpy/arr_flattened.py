"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 15:50:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create a contiguous flattened array.
"""
import numpy as np

arr1=np.array([[10,20,30],[40,50,60]])
print(arr1)
flat_arr=np.ravel(arr1)
print(flat_arr)