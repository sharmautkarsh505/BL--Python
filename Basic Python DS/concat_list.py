"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 10:11:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to concatenate all elements in a list into a string and return it.
"""

def concat_list(input_list):
    string=''
    for element in input_list:
        string+=element
    return string


def take_input():
    input_list=[]
    input_list=[ele for ele in input('Enter list elements: ').split(',')]
    return input_list

print(concat_list(take_input()))