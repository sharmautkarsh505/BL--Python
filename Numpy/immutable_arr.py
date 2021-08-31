"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 16:28:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to make an array immutable (read-only).
"""
import numpy as np

arr_1=np.arange(1,11)
arr_1.flags.writeable=False
#changing the value will reflect error
arr_1[1]=4