"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-25 10:11:00
Last Modified by:----
Last Modified time:----
Title : Matrix operations
"""
def matrix_operations():
    
    class NegativeInputError(Exception):
        pass   
    try:  
        i=int(input('Rows: '))
        j=int(input('Columns: '))
        matrix_1= [["_" for _ in range(j)] for _ in range(i)]
        for r_index in range(i):
            for c_index in range(j):
                matrix_1[r_index][c_index] = int(input('Enter element : '))
        m=int(input('Rows: '))
        n=int(input('Columns: '))
        matrix_2= [["_" for _ in range(n)] for _ in range(m)]
        for r_index in range(m):
            for c_index in range(n):
                matrix_2[r_index][c_index] = int(input('Enter element : '))
        if i<1 and j<1:
            raise NegativeInputError
        if m<1 and n<1:
            raise NegativeInputError
    except NegativeInputError:
        print('Please enter positive integer values for the rows and columns')
    except ValueError:
        print('Please enter integer values for the rows and columns')
    except Exception:
        print('Please enter valid inputs')

    if i==m and j==n: 
        add_result=[[matrix_1[i][j]+matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
        print(add_result)
        sub_result=[[matrix_1[i][j]-matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
        print(sub_result)
    else:
        pass

    if j==m:
        multiply_result=[[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    multiply_result[i][j]+=matrix_1[i][k]*matrix_2[k][j]

        print(multiply_result)
    else:
        pass

    
matrix_operations()