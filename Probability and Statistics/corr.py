"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-28 03:07:00
Last Modified by:----
Last Modified time:----
Title :Correlation between height and the pulse rate
"""
import statistics as st 
import math
#reps height
x=[68,72,65,70,62,75,78,64,68]
#reps pulse rate
y=[90,85,88,100,105,98,70,65,72]

mean_x=st.mean(x)
print(mean_x)
mean_y=st.mean(y)
print(mean_y)

#defining correlation coefficient
numerator=0
denominator=0
for i in range(9):
    numerator+=(x[i]-mean_x)*(y[i]-mean_y)
    denominator+=math.sqrt(pow(x[i]-mean_x,2))*(pow(y[i]-mean_y,2))

corr=numerator/denominator
print(corr)

#conclusion: the correlation bw the height and pulse rate is very weak 