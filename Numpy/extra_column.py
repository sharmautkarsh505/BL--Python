"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 17:42:00
Last Modified by:----
Last Modified time:----
Title: Write a Python program to how to add an extra column to an numpy array.
"""
import numpy as np

arr1=np.arange(4).reshape((2,2))
arr2=np.array([4,5])
new_arr=np.column_stack((arr1,arr2))
print(new_arr)