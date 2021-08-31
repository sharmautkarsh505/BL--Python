"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 15:33:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to save a NumPy array to a text file.
"""
import numpy as np

arr1=np.array(list(range(1,11)))
np.savetxt('numpy_save.txt',arr1)