"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-13 12:07:00
Last Modified by:---
Last Modified time:----
Title : Write a Python function that takes a list of words and returns the length of the longest
one.
"""
player_names=['Jimmy Butler','Kevin Durant','DeAndre Jordan','Kyle Lowry','Harrison Barnes',
            'DeMar DeRozan','Kyrie Irving','Klay Thompson','DeMarcus Cousins',
             'Paul George','Draymond Green','Carmelo Anthony']

player_dict={}
for player in player_names:
    player_dict[player]=len(player)

print(max(player_dict,key=player_dict.get))


    