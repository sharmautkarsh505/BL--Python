"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 03:04:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""
import matplotlib.pyplot as plt

x=list(range(1,11))
y=[i for i in x]

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=x OR x=y')
plt.show()