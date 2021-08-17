"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 19:30:00
Last Modified by:----
Last Modified time:----
Title : Find the harmonic sum, till the number input by user
"""
try:
   number=int(input("Enter number:"))

   if number<0:
      raise Exception

   hsum=0.0
   for x in range(1,number+1):
      hsum=hsum+(1/x)

   print(hsum)

except Exception:
   print('Invalid input.Please enter a positive integer')
