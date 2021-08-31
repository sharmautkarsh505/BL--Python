"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 17:29:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to convert a NumPy array into Python list structure.
"""
import numpy as np

arr1=np.array([0.26153123,0.52760141,0.5718299,0.5927067,0.7831874,0.69746349,0.35399976,0.99469633,0.0694458,0.54711478])
round_off_arr=arr1.round(3)
print(round_off_arr)
arr1_list=arr1.round(3).tolist()
print(arr1_list)
