"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 18:16:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
"""
import numpy as np

arr_zeroes=np.zeros((8,8))

#pattern for rows 0,2,4,6
for i in range(0,8,2):
    for j in range(1,9,2):
        arr_zeroes[i][j]=1

#pattern for rows 1,3,5,7
for i in range(1,9,2):
    for j in range(0,8,2):
        arr_zeroes[i][j]=1

print(arr_zeroes)