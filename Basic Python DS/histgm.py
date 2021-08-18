"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-11 10:04:00
Last Modified by:---
Last Modified time:----
Title :Write a Python program to create a histogram from a given list of integers.
"""

def hist_plot(num_list):
    for i in num_list:
        empty_s=''
        count=i
        while count>0:
            empty_s+='|'
            count-=1
        print(empty_s)

hist_plot([2,4,6,8])