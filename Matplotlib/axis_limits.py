"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 13:50:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to display the current axis limits values and set new axis values.
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,101)
exp_x=np.exp(x)

plt.plot(x,exp_x)
plt.xlabel('x')
plt.ylabel('e^x')
plt.title('Exponent')
print(plt.xlim())
plt.xlim((0,10))
plt.ylim((0,24000))
plt.show()