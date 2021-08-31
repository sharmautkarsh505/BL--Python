""""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 10:51:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create a 2d array with 1 on the border and 0 inside.
"""
import numpy as np

matrix_ones_5x5=np.ones((5,5))
matrix_ones_5x5[1:-1,1:-1]=0
print(matrix_ones_5x5)