"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 10:06:00
Last Modified by:----
Last Modified time:----
Title : Create a 3x3 matrix with values ranging from 2 to 10.
"""
import numpy as np


matrix_3x3=np.array([[1,2,3],[4,5,6],[7,8,9]])
#or 
matrix_3x3_new=np.arange(1,10).reshape((3,3))
print(matrix_3x3)
print(matrix_3x3_new)