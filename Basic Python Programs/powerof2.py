"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 19:00:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 15:11:00
Title : find the powers of two till input number
"""
try:
    #enter the number of powers of 2 wanted
    number=int(input('Enter a number:'))
    
except ValueError:
    print('Please enter an integer value')
except Exception:
    print('Please enter a valid input')

else:
    #initiating empty list
    powers=[]
    #parse through entire range and append to the empty list
    for x in range(0,number+1):
        powers.append(pow(2,x))
    print(powers)