"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 23:11:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to select the specified columns and rows from a given data
frame. Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
"""
import numpy as np
import pandas as pd

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data=pd.DataFrame(exam_data,index=labels)
data.drop(['a','c','e','f'],axis=0,inplace=True)
data.drop(['attempts','qualify'],axis=1,inplace=True)
print(data)