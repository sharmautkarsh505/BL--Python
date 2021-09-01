"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-09-01 15:21:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create multiple plots.
"""
import matplotlib.pyplot as plt
import numpy as np 


arr_x=np.arange(1,11)

arr_y1=np.power(arr_x,2)
arr_y2=np.power(arr_x,3)
arr_y3=np.log(arr_x)
arr_y4=np.exp(arr_x)

fig,ax=plt.subplots(2,2)

ax[0,0].plot(arr_x,arr_y1)
ax[0,0].set_title('x^2')

ax[1,0].plot(arr_x,arr_y2)
ax[1,0].set_title('x^3')

ax[0,1].plot(arr_x,arr_y3)
ax[0,1].set_title('log(x)')

ax[1,1].plot(arr_x,arr_y4)
ax[1,1].set_title('e^x')

fig.tight_layout()
plt.show()

