"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-26 11:52:00
Last Modified by:----
Last Modified time:----
Title : Find the probability of drawing an ace after drawing an ace on
the first draw
"""

cards_in_deck=52

aces_in_deck=4

prob_ace_1=4/52
prob_ace_2=3/51

prob_ace1_ace2=prob_ace_1*prob_ace_2
print(prob_ace1_ace2)