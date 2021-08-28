"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-28 05:27:00
Last Modified by:----
Last Modified time:----
Title :A radar unit is used to measure speeds of cars on a motorway. The speeds are
normally distributed with a mean of 90 km/hr and a standard deviation of 10 km/hr. Write a
program to find the probability that a car picked at random is travelling at more than 100 km/hr.
"""
#random variable will represent speed of cars
from statistics import NormalDist
#using mean and std define the normal distribution
sat=NormalDist(90,10)
#using cdf compute probability of speed being greater than 100 kmph
p_g100=1-sat.cdf(100)
print(p_g100)