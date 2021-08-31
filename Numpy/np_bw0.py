""""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 11:30:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to add a border (filled with 0's) around an existing array.
"""
import numpy as np 

matrix_ones_3x3=np.ones((3,3))
matrix_padded=np.pad(matrix_ones_3x3,((1,1),(1,1)),mode='constant',constant_values=0)

print(matrix_padded)