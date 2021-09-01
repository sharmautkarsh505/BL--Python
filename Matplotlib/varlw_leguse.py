"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 13:00:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to plot two or more lines with legends, different widths and colors.
"""
import matplotlib.pyplot as plt

x=list(range(1,11))
y=[i for i in x]
z=[i*2 for i in x]

plt.plot(x,y,lw=3,label='y',color='steelblue')
plt.plot(x,z,lw=5,label='z',color='grey')
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('y,z')
plt.title('Relationship between x,y and x,z')
plt.show()