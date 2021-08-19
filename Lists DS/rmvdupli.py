"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 17:04:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to remove duplicates from a list.
"""
my_list=[2, 5, 1, 2, 4, 4, 2, 3, 2, 1]

updtd_list=[]
[updtd_list.append(x) for x in my_list if x not in updtd_list]

print(updtd_list)