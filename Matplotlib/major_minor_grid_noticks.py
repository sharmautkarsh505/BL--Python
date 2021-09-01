"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 14:22:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to display the grid and draw line charts of the closing value of
Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn
off ticks.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('fdata.csv')
data.drop(labels=data.iloc[:,1:4],axis=1,inplace=True)
print(data)

plt.plot(data['Date'],data['Close'])
plt.xlabel('Date (dd-mm-yyyy)')
plt.ylabel('Closing Price')
plt.title('Closing Price trend of Alphabet Inc.')
plt.grid(which='minor',lw=0.2,ls=':',color='red')
plt.grid(which='major',lw=0.3,ls="-",color='black',alpha=0.9)
plt.minorticks_on()
plt.tick_params(which='both',top=False,left=False,bottom=False)

plt.show()
