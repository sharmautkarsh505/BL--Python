"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 11:27:00
Last Modified by:---
Last Modified time:----
Title : Write a program to get execution time for a Python method.
"""

import timeit

def powers2(n):
    start_time=timeit.default_timer()
    powers=[]
    [powers.append(2**i) for i in range(1,n+1)]
    end_time=timeit.default_timer()
    return powers,end_time-start_time

print(powers2(10))
