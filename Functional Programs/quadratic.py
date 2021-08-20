"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 21:00:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 17:48:00
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
    try:
        a,b,c=input('Enter the numbers:').split(',')
        sol_quadraticeqn(float(a),float(b),float(c))
    except ValueError:
        print('Please enter integer or float values')
    except Exception:
        print('Please enter valid inputs')