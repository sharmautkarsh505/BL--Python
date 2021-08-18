"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 08:53:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
"""

first_name,last_name=input('Enter Full name:').split()

while first_name.isalpha() and last_name.isalpha():
    print(f'{last_name} {first_name}')
    break
