"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-07 20:00:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-20 15:59:00
Title : A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
"""
def make_array(row,column):
    array = [["_" for _ in range(column)] for _ in range(row)]
    for r_index in range(row):
        for c_index in range(column):
            array[r_index][c_index] = int(input('Enter element : '))
    for r_index in array:
        print(r_index)

try:  
    make_array(int(input('Rows: ')),int(input('Columns: ')))
except ValueError:
    print('Please enter integer values for the rows and columns')
except Exception:
    print('Please enter valid inputs')