"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:00:00
Last Modified by:---
Last Modified time:----
Title : A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
"""
def make_array(row,column):
    array = [[0 for c_index in range(column)] for r_index in range(row)]
    for r_index in range(row):
        for c_index in range(column):
            array[r_index][c_index] = int(input('Enter element : '))
    for r_index in array:
        print(r_index)
        
make_array(int(input('Rows: ')),int(input('Columns: ')))