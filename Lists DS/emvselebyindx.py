"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 17:44:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
"""
colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#colours.pop(0)
#colours.pop(3)
#colours.pop(3)

#print(colours)

colours.remove('Red')
colours.remove('Pink')
colours.remove('Yellow')

print(colours)