"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 16:08:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to create an array which looks like below array.
"""
import numpy as np

lower_triangular_matrix=np.tril(np.ones((3,3)),k=0)
np.fill_diagonal(lower_triangular_matrix,val=0)
print(lower_triangular_matrix)

l_matrix=np.tril(np.ones((4,3)))
print(l_matrix)
np.fill_diagonal(l_matrix,val=0)
print(l_matrix)