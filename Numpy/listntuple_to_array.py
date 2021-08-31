"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 09:59:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to convert a list and tuple into arrays.
"""
import numpy as np

num_list=list(range(1,11))
num_tuple=tuple(num_list)

l2_arr=np.array(num_list)
t2_arr=np.array(num_tuple)
print(l2_arr)
print(t2_arr)