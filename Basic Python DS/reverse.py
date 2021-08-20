"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 08:53:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-21 02:38:00
Title : Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
"""
class UnacceptedInputError(Exception):
    pass
    
try:
    first_name,last_name=input('Enter Full name:').split()

    if first_name.isalpha()==False and last_name.isalpha()==False:
        raise UnacceptedInputError
    
except UnacceptedInputError:
    print('Please enter an alphabetical input')
except Exception:
    print('Please enter a valid input')
else:
    print(f'{last_name} {first_name}')
