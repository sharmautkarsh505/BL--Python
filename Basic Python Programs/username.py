"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 17:30:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20- 11:00:00
Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""
try:
    user_name=input('Please enter your username:\n')
    if len(user_name) <3:
        raise TypeError
except TypeError:
    print('Please enter a valid input')
else:
    print(f"Hello {user_name}, How are you?")
