"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 22:54:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to convert a Panda module Series to Python list and it's type.
"""
from numpy import dtype
import pandas as pd

series_1=pd.Series([1,2,3,4])
s_list=series_1.tolist()
print(s_list)
print(dtype(s_list))
