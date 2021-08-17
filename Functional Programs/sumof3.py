"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:20:00
Last Modified by:---
Last Modified time:----
Title : A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0 
"""
def sum_of_three(elements):
    array = [0 for index in range(elements)]
    for index in range(elements):
        array[index] = int(input('Enter element : '))
        print(array)
        for i in range(elements):
            j = i+1
            for j in range(j,elements):
                k = j+1
                for k in range(k,elements):
                    if array[i] + array[j] + array[k] == 0 :
                        print(array[i] , array[j], array[k])


sum_of_three(int(input('Enter number of elements : ')))