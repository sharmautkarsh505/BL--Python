"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 15:20:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to extract single key-value pair of a dictionary in variables.
"""

player_stats_dictionary={'Lebron James':16.2,'Stephen Curry':32.8,'Damian Lillard':24.8}

key, value = next(iter(player_stats_dictionary.items()))
print(key,value)