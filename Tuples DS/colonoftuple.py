"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 09:52:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to create the colon of a tuple.
"""
from copy import deepcopy

#define tuple x
tuple_n = ("Kyrie Irving", [],'6', False) 

#deepcopy makes copy of tuple_x
tuple_n_colon = deepcopy(tuple_n)
#makes [] [50]
tuple_n_colon[1].append(10)
print(tuple_n_colon)
