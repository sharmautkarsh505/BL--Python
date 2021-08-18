"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 10:30:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

#what remains in set color_list_1 after intersection elements b/w are removed
print(color_list_1.difference(color_list_2))
#what remains in set color_list_2 after intersection elements are removed
print(color_list_2.difference(color_list_1))

#For multiple sets
color_list_3=['Red','Blue','Violet']
print(color_list_1.difference(color_list_2,color_list_3))

