"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 02:39:00
Last Modified by:----
Last Modified time:----
Title:Write a Python program to iterate over rows in a DataFrame.
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
for index,row in data.iterrows():
    print(row['name'],row['score'],row['attempts'],row['qualify'])
