"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 09:34:00
Last Modified by:---
Last Modified time:----
Title : Write a Python script to sort (ascending and descending) a dictionary by value.
"""
dict={}

#A dictionary of nba players and the points they scored in 2020-21 nba season
dict['Damian Lillard']=1928
dict['Stephen Curry']=2015
dict['Julius Randle']=1712
dict['Bradley Beal']=1878
dict['Kyrie Irving']=1451


points=dict.values()
print(points)
#Ascending order 
asc_sorted={}
for i,j in sorted(dict.items(),key=lambda item:item[1]):
    asc_sorted[i]=j
print(asc_sorted)

#Descending order
dsc_sorted={}
for i,j in sorted(dict.items(),key=lambda item:item[1],reverse=True):
    dsc_sorted[i]=j
print(dsc_sorted)
