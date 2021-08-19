"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 11:03:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to create a dictionary from a string.
"""
string='damianlillard'

dict={}

for element in string:
    dict[element]=string.count(element)

print(dict)