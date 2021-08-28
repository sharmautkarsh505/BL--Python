"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-26 11:01:00
Last Modified by:----
Last Modified time:----
Title : Find the probability of drawing an ace after drawing a king on
the first draw
"""
cards_in_deck=52

aces_in_deck=4

kings_in_deck=4

prob_king=4/52
prob_ace=4/51

prob_king_ace=prob_king*prob_ace
print(prob_king_ace)