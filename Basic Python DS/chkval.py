"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 09:56:00
Last Modified by:2021-08-18 12:06:00
Last Modified time:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Title : Write a Python program to check whether a specified value is contained in a group of values.
"""

def check_value(number):
    values=list(range(1,11))
    for value in values:
        if value==number:
            return True
        else:
            pass


print(check_value(int(input('Enter the number:'))))
    