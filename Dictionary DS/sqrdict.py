"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 10:16:00
Last Modified by:---
Last Modified time:----
Title : Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
"""
dict={}

n=int(input('Enter number:'))

for i in range(1,n+1):
    dict[i]=i**2

print(dict)