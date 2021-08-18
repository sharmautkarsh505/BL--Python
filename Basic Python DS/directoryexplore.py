"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 11:15:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to list all files in a directory in Python.
"""

try:
    import os
except Exception:
    print('Error in importing module')
try:
    #exploring method isspace in the python directory
    print(os.listdir(r'C:\Users\utkarsh.sharma\AppData\Local\Microsoft'))
except Exception:
    print('Error')