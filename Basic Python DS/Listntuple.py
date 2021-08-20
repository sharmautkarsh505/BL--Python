"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 14:02:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-21 02:47:00
Title : Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
"""
try:
    input_list=[]
    input_list=input('Enter numbers:').split(',')
    input_list=[int(i) for i in input_list]
except Exception:
    print('Invalid input')
else:
    print(input_list)
    print(tuple(input_list))
    
