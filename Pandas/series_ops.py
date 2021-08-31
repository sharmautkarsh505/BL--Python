"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 22:58:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to add, subtract, multiple and divide two Pandas Series.
"""
from numpy import multiply
import pandas as pd

series_1=pd.Series([2, 4, 6, 8, 10])
series_2=pd.Series([1, 3, 5, 7, 9])

add_series=series_1+series_2
sub_series=series_1-series_2
mul_series=series_1*series_2
div_series=series_1/series_2