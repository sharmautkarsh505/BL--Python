"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 13:08:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to find common values between two arrays.
"""
import numpy as np

arr1=np.array([0,10,20,40,60]) 
arr2=np.array([10,30,40])
intersection_arr=np.intersect1d(arr1,arr2)
print(intersection_arr)