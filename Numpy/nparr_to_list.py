"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 16:38:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to convert a NumPy array into Python list structure.
"""
import numpy as np

arr1=np.arange(0,6).reshape((3,2))
arr_to_list=arr1.tolist()
print(arr_to_list)