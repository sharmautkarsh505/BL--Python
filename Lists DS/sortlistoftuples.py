"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 16:47:00
Last Modified by:----
Last Modified time:----
Title :Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
"""
sample_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

ordered_list=sorted(sample_list,key=lambda x: x[1])
print(ordered_list)
