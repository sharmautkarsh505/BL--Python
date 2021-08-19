"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 13:17:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to remove an item from a set if it is present in the set.
"""
basketball_players={'Lebron James','Kyrie Irving','John Wall','Jayson Tatum','Kyle Lowrie','Kevin Durant'}

for player in basketball_players:
    if player=='Jayson Tatum':
        basketball_players.remove('Jayson Tatum')
        break

print(basketball_players)
