"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 12:12:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to get the size of an object in bytes.
"""

import sys
import numpy as np

d1='Hello world'
num1=23
num_list=list(range(1,11))
str_list=['take','two','interactive']
num_array=np.array(list(range(1,11)))

print("Bytes in d1: ",sys.getsizeof(d1))
print("Bytes in num1: ",sys.getsizeof(num1))
print("Bytes in num_list: ",sys.getsizeof(num_list))
print("Bytes in str_list: ",sys.getsizeof(str_list))
print("Bytes in num_array: ",sys.getsizeof(num_array))