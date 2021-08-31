"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 17:37:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-31 17:56:00
Title :Write a Python program to suppresses the use of scientific notation for small
numbers in numpy array.
"""
import numpy as np
np.set_printoptions(suppress=True)
my_arr=np.array([1.60000000e-10,1.60000000e+00,1.20000000e+03,2.35000000e-01])
print(my_arr)