"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 09:51:00
Last Modified by:----
Last Modified time:----
Title :Write a Python script to concatenate following dictionaries to create a new
one.
"""
dict1={}
dict1['Damian Lillard']=1928
dict1['Stephen Curry']=2015
dict2={}
dict2['Julius Randle']=1712
dict2['Bradley Beal']=1878
dict3={}
dict3['Kyrie Irving']=1451
dict3['Jayson Tatum']=1692

res=dict1|dict2|dict3
print(res)