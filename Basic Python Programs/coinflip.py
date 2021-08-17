"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 18:00:00
Last Modified by:Utkarsh Sharma
Last Modified time:2021-08-10 10:00:00
Title : Flip Coin and print percentage of Heads and Tails
"""
#Import random fuction to ensure arbitrariness
import random

#User inputs the number of times the coin will be tossed
n_flips=int(input('Number of times the coin is tossed:'))
#Intiate variable that reflects the number of heads in N tosses
head=0
#Intiate variable that reflects the number of tails in N tosses 
tail=0
#Conditional to check the number of heads and tails that come after all tosses
for x in range(1,n_flips+1):
    #pr will be 0 or 1, if 0 turns up,its heads, if 1 turns up,its tails
    pr=random.randint(0,1)
    if pr==0:
        #Increase the count of heads
        head+=1
    else:
        #increase the count of tails
        tail+=1

#Calculating perc of head and tails in all N tosses, where N is the user input
percentage_heads=round((head/(n_flips))*100,2)
percentage_tails=round((tail/(n_flips))*100,2)

#Printing the perc
print(f"Heads:{percentage_heads}%")
print(f"Tails:{percentage_tails}%")