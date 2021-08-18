"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 11:44:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to sort three integers without using conditional statements and loops.
"""

a,b,c=input('Enter 3 integers:').split(',')

numbers=[]
numbers.append(int(a))
numbers.append(int(b))
numbers.append(int(c))
print(sorted(numbers))

