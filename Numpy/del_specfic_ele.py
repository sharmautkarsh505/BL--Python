"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 17:47:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to remove specific elements in a numpy array.
"""
import numpy as np

arr1=np.arange(10,110,10)
index=[0,3,4]
new_arr=np.delete(arr1,index)
print(new_arr)

