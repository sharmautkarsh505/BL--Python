"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:30:00
Last Modified by:---
Last Modified time:----
Title : Find the euclidean distance of a point in the x-y plane with respect to the origin 
"""
import cmath 
import logging

logging.basicConfig(filename='eucdistchk.log',level=logging.INFO)

def euclidean_distance(x,y):
    #Distance of the point from the origin
    dist=cmath.sqrt((x**2)+(y**2))
    logging.info(dist)
  
while True:
    x,y=input('Enter the co-ordinates of the point:').split()
    euclidean_distance(int(x),int(y))