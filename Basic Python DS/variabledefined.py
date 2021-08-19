"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 13:02:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to determine if variable is defined or not.
"""
#defined variable
try:
    num_list=list(range(2,12,2))

except NameError:
    print('Variable not defined')
except Exception:
    print('Invalid')
else:
    print('Vaiable is defined')

#not defined 
try:
    sum=pm
except NameError:
    print('Variable not defined')
except Exception:
    print('Invalid')
else:
    print('Variable is defined')
