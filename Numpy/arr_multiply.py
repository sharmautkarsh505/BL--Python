"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 16:33:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array.
"""
import numpy as np

my_arr=np.arange(0,12).reshape((3,4))
new_arr=my_arr*3
print(new_arr)