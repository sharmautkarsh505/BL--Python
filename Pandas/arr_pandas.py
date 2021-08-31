"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 22:46:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to create and display a one-dimensional array-like object
containing an array of data using Pandas module.
"""
import pandas as pd

df1=pd.Series(list(range(1,6)))
print(df1)