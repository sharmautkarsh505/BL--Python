"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 15:56:00
Last Modified by:----
Last Modified time:----
Title: Write a Python program to change the data type of an array.
"""
import numpy as np 

arr1=np.arange(2,14,2).reshape((2,3))
print(arr1.dtype)
arr1=arr1.astype('float')
print(arr1)
print(arr1.dtype)