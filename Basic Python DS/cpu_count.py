"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 11:05:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to find out the number of CPUs using
"""
try:
    import multiprocessing
    print(multiprocessing.cpu_count())
except NotImplementedError:
    print('Method has not been implemented yet')
except Exception:
    print('Error')