"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-26 10:19:00
Last Modified by:----
Last Modified time:----
Title : is a normally normally distributed variable with mean μ = 30 and standard
deviation σ = 4. Write a program to find P(x < 40),P(x > 21),P(30 < x < 35)
"""
from statistics import NormalDist

sat=NormalDist(30,4)
#cdf for p(x<40)
p_l40=sat.cdf(40)
print(p_l40)
#as the cdf func of python calculates p<21,subtract that probability from 1 to obtain the P(x>21)
p_g21=1-sat.cdf(21)
print(p_g21)
#find probability for x>30 and the x<35 and subtract
p_g30=1-sat.cdf(30)
p_l35=sat.cdf(35)
p_30x35=p_l35-p_g30
print(p_30x35)
