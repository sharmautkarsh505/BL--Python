"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 23:03:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to get the powers of an array values element-wise.
"""
import numpy as np
import pandas as pd

arr1=np.arange(7)
pwr_arr=np.power(arr1,3)
print(pwr_arr)

series_1=pd.Series(list(range(7)))
pwr_series=series_1**3
print(pwr_series)