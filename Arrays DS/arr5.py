"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 16:18:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""
import array

arr5=array.array('i',[1,2,3,4,5])
for i in range(0,5):
    print(arr5[i])
    i+=1


