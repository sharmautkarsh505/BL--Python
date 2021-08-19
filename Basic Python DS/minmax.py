"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 16:04:00
Last Modified by:----
Last Modified time:----
Title : Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
"""
def minmax(data):
    minimum=data[0]
    maximum=data[0]
    for number in data:
        if number>maximum:
            maximum=number
        elif number<minimum:
            minimum=number
    return minimum,maximum

print(minmax([12,3,56,7,9,-1,84]))