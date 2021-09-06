"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 13:18:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to plot two or more lines and set the line markers.
line.
"""
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('fdata.csv')
print(data)
plt.plot(data['Date'],data.iloc[:,1:],label=['Open','High','Low','Close'],marker='.')
plt.xlabel('Date(dd-mm-yyyy)')
plt.legend(loc=0)
plt.title('Stock price trend Alphabet Inc.')
plt.show()
