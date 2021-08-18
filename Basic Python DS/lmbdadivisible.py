"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 14:02:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

number_list=[122,225,75,625,90]

divisible_list=list(filter(lambda x: x%15==0,number_list))
print(divisible_list)