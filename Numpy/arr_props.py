"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 09:59:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to find the number of elements of an array, length of one
array element in bytes and total bytes consumed by the elements.
"""
import numpy as np

num_arr=np.arange(6).reshape(2,3)
n_elements=num_arr.size
len_item=num_arr.itemsize
bytes_elements=num_arr.nbytes
print(n_elements,len_item,bytes_elements)