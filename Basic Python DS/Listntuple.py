"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 14:02:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-18 16:03:00
Title : Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
"""

#could the user input any number of numbers
#do not need to change the input to integer as in the sample list all elements are strings 
input_string=input('Enter numbers seperated by comma:')
input_list=[]
input_list=input_string.split(',')
print(input_list)
print(tuple(input_list))
