"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 03:04:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to draw a line using given axis values taken from a text file, with
suitable label in the x axis, y axis and a title.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=np.loadtxt('test.txt')
df=pd.DataFrame(data,columns=['x','y'])

plt.plot(df['x'],df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Relationship between x and y')
plt.show()