"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 21:00:00
Last Modified by:---
Last Modified time:----
Title : Find the roots of the quadratic equation on the basis of the coefficients and constants provided by the user
"""
import cmath
import logging

logging.basicConfig(filename='rootschk.log',level=logging.INFO,format='%(asctime)s:%(name)s:%(message)s')

def sol_quadraticeqn(a,b,c):
    delta=(b**2)-(4*a*c)
    root_1=(-b+cmath.sqrt(delta))/(2*a)
    root_2=(-b-cmath.sqrt(delta))/(2*a)
    logging.info(f'The roots of the quadratic equation are {root_1} and {root_2}')

while True:
    a,b,c=input('Enter the numbers:').split()
    sol_quadraticeqn(int(a),int(b),int(c))