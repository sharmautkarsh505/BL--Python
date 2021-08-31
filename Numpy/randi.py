""""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-31 10:11:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to find the real and imaginary parts of an array of complex numbers.
"""
import numpy as np

complex_numbers=np.array([1.00000000+0.j,0.70710678+0.70710678j])
real_parts=complex_numbers.real
imaginary_parts=complex_numbers.imag

print(real_parts)
print(imaginary_parts)