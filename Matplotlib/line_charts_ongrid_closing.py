"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 14:14:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to display the grid and draw line charts of the closing value of
Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
linestyle -, width .5. and color blue.
"""
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('fdata.csv')
data.drop(labels=data.iloc[:,1:4],axis=1,inplace=True)
print(data)

plt.plot(data['Date'],data['Close'])
plt.xlabel('Date(dd-mm-yyyy)')
plt.title('Closing stock price trend Alphabet Inc.')
plt.grid(ls='-',lw=0.5,color='blue')
plt.show()