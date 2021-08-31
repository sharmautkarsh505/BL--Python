"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 09:59:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to append values to the end of an array.
"""
import numpy as np 

arr1=np.array([10,20,30])
arr1=np.append(arr1,[40,50,60,70,80,90],axis=0)
print(arr1)