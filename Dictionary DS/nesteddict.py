"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 11:49:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to convert a list into a nested dictionary of keys.
"""
num_list=list(range(1,11))
dict=new={}

for number in num_list:
    new[number]={}
    new=new[number]

print(dict)
