"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 10:04:00
Last Modified by:---
Last Modified time:----
Title : Write a Python program to iterate over dictionaries using for loops.
"""
dict={'Damian Lillard':1928,
      'Stephen Curry':2015,
      'Julius Randle':1712,
      'Bradley Beal':1878,
      'Kyrie Irving':1451, 
      'Jayson Tatum':1692}

for key,value in dict.items():
    print('Player:',key)
    print('Points scored:',value)

