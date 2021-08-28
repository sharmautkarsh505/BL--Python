"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-26 11:52:00
Last Modified by:----
Last Modified time:----
Title : You toss a fair coin three times write a program to find following
What is the probability of three heads, HHH?
What is the probability that you observe exactly one heads?
Given that you have observed at least one heads, what is the probability
that you observe at least two heads?
"""
from itertools import product

#no of tosses
n=3 
#sample space 
omega=set(product({'H','T'},repeat=3))
#total no of elments in sample  space 
print(omega)

event_3h={event for event in omega if event.count('H')==3}
event_1h={event for event in omega if event.count('H')==1}
event_m2h={event for event in omega if event.count('H')>=2}
def prob(X):
    return len(X)/len(omega)


print(prob(event_3h))
print(prob(event_1h))
print(prob(event_m2h))