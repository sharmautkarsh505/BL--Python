"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:00:00
Last Modified by:---
Last Modified time:----
Title : Find the factors of the given number
"""
#Enter the number that need to be factorized
number=int(input('Enter number:'))
#List of possible factors 
possible_factors=list(range(1,number+1,1))
#Intiate an empty list for the factors 
factors=[]

#Iterate through the list of possible factors 
for possible_factor in possible_factors:
    #Divisibility check
    if number%possible_factor==0:
        #Add to the empty list
        factors.append(possible_factor)

#Show the factors
print(factors)