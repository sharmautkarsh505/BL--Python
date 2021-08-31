""""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 10:17:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to reverse an array (first element becomes last).
"""
import numpy as np

num_arr=np.array([12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
res=num_arr[::-1]
#or 
res_1=np.flip(num_arr,axis=0)
#or
res_2=np.flipud(num_arr)