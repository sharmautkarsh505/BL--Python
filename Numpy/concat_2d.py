"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 16:26:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to concatenate two 2-dimensional arrays.
"""
import numpy as np

arr_1=np.array([[0,1,3],[5,7,9]])
arr_2=np.array([[0,2,4],[6,8,10]])
concat_arr=np.concatenate((arr_1,arr_2),axis=1)
print(concat_arr.shape)
print(concat_arr)
