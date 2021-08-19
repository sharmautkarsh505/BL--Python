"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 10:20:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to check whether an element exists within a tuple.
"""

dummy_tuple=tuple(range(1,11,2))

number=int(input('Input number: '))
for element in dummy_tuple:
    if number==element:
        print('Element exists in the tuple')
    else:
        pass