"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:00:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 15:33:00
Title : Find the factors of the given number
"""
try:
#Enter the number that need to be factorized
    number=int(input('Enter number:'))

except ValueError:
    print('Enter an integer value')

else:
    #List of possible factors 
    if number>1:
        possible_factors=list(range(1,number+1,1))
        #Intiate an empty list for the factors 
        factors=[]

        #Iterate through the list of possible factors 
        for possible_factor in possible_factors:
            #Divisibility check
            if number%possible_factor==0:
                #Add to the empty list
                factors.append(possible_factor)
        print(factors)
    elif number<1:
        possible_factors=list(range(1,(number)*(-1)+1,1))
        #Intiate an empty list for the factors 
        possible_negative_factors=list(range(-1,number-1,-1))
        factors=[]

        #Iterate through the list of possible factors 
        for possible_factor in possible_factors:
            #Divisibility check
            if number%possible_factor==0:
                #Add to the empty list
                factors.append(possible_factor)
        for possible_negative_factor in possible_negative_factors:
            if number%possible_negative_factor==0:
                factors.append(possible_negative_factor)

        print(factors)