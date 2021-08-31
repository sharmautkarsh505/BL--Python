"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 03:04:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to draw a line with suitable label in the x axis, y axis and a title
"""
import matplotlib.pyplot as plt

temp_celsius=list(range(-88,59))
temp_fahrenheit=[((temp*(9/5))+32) for temp in temp_celsius]

plt.plot(temp_celsius,temp_fahrenheit)
plt.xlabel('Temperature in Celsius')
plt.ylabel('Temperature in Fahrenheit')
plt.title('Relationship between temperature in Celsius and Fahrenheit')
plt.show()