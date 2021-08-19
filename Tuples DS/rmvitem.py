"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 10:49:00
Last Modified by:----
Last Modified time:----
Title: Write a Python program to remove an item from a tuple.
"""

arbitrary_tuple=(1,122,11,4,5,90,5,6,8,7,5)

arbitrary_list=list(arbitrary_tuple)
arbitrary_list.pop(1)
arbitrary_tuple=tuple(arbitrary_list)
print(arbitrary_tuple)
