"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 17:30:00
Last Modified by:----
Last Modified time:----
Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
"""
#User inputs his/her username
user_name=input('Please enter your username:\n')

#Conditional to ensure that user name is a string, is greater than 3 chars and has a space(for full name)
if type(user_name)==str and len(user_name)>=3:
    print(f"Hello {user_name}, How are you?")
else:
    print("Invalid input")
