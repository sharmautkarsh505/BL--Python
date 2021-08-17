"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 19:00:00
Last Modified by:----
Last Modified time:----
Title : find the powers of two till input number
"""
#enter the number of powers of 2 wanted
number=int(input('Enter a number:'))
#initiating empty list
powers=[]
#parse through entire range and append to the empty list
for x in range(0,number+1):
    powers.append(pow(2,x))
print(powers)