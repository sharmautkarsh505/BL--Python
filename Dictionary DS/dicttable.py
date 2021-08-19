"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 11:20:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to print a dictionary in table format.
"""
dict={1:['Damian Lillard',1928,28.8],
      2:['Stephen Curry',2015,32.0],
      3:['Julius Randle',1712,24.1],
      4:['Bradley Beal',1878,31.3],
      5:['Kyrie Irving',1451,26.9],
      6:['Jayson Tatum',1692,26.4]}

print('{:10} {:10} {:10}'.format('PLAYER','POINTS','PPG'))

for k,v in dict.items():
    player,points,ppg=v
    print('{:10} {:10} {:10}'.format(player,points,ppg))

    


