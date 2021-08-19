"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-12 16:34:00
Last Modified by:----
Last Modified time:----
Title : Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
"""
sample_list= ['abc', 'xyz', 'aba', '1221']
count=0
for sample in sample_list:
    if len(sample)>=2 and sample[0]==sample[len(sample)-1]:
        count+=1

print(count)

