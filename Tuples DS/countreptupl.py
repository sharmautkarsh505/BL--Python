"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 10:07:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to find the repeated items of a tuple.
"""
arbitrary_tuple=(1,122,11,4,5,90,5,6,8,7,5)

for element in arbitrary_tuple:
    if arbitrary_tuple.count(element)>1:
        print(element)
        break
    else:
        pass