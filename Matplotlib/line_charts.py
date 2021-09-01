"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 03:04:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('fdata.csv')
print(data)
plt.plot(data['Date'],data.iloc[:,1:])
plt.xlabel('Date(dd-mm-yyyy)')
plt.text(x=-0.17,y=768.95,s='Low')
plt.text(x=-0.2,y=772,s='Close')
plt.text(x=-0.2,y=773.72,s='Open')
plt.text(x=-0.17,y=775.40,s='High')
plt.title('Stock price trend Alphabet Inc.')
plt.show()



