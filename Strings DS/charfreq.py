"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 11:31:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to count the number of characters (character frequency) in a string.
"""

player_name='Kyrie Irving'

#Initiate empty dictionary
res={}

for keys in player_name:
    res[keys]=res.get(keys,0)+1

print(res)
