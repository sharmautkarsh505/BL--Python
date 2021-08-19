"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 18:03:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to generate all permutations of a list in Python.
"""
from itertools import permutations
colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

perms=permutations(colours)

for perm in list(perms):
    print(perm)

