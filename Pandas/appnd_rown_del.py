"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 00:58:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to append a new row 'k' to data frame with given values for
each column. Now delete the new row and return the original DataFrame.
"""
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data=pd.DataFrame(exam_data,index=labels)
df=pd.DataFrame({'name' :'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'},index=['k'])
data=data.append(df)
print(data)
data.drop(['k'],inplace=True)
print(data)
