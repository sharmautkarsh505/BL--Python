"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-25 10:11:00
Last Modified by:----
Last Modified time:----
Title : Matrix operations
"""
def matrices_operations():
    
    class NegativeInputError(Exception):
        pass   
    try:  
        i=int(input('Rows: '))
        j=int(input('Columns: '))
        if i<1 and j<1:
            raise NegativeInputError
        matrix_1= [["_" for _ in range(j)] for _ in range(i)]
        for r_index in range(i):
            for c_index in range(j):
                matrix_1[r_index][c_index] = int(input('Enter element : '))
        m=int(input('Rows: '))
        n=int(input('Columns: '))
        if m<1 and n<1:
            raise NegativeInputError
        matrix_2= [["_" for _ in range(n)] for _ in range(m)]
        for r_index in range(m):
            for c_index in range(n):
                matrix_2[r_index][c_index] = int(input('Enter element : '))
        

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
        print('The order of the matrices is incompatible for addition and subtraction')

    if j==m:
        multiply_result=[[0 for _ in range(len(matrix_2[0]))] for _ in range(len(matrix_1))]
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])):
                for k in range(len(matrix_2)):
                    multiply_result[i][j]+=matrix_1[i][k]*matrix_2[k][j]

        print(multiply_result)
    else:
        print('The order of the matrices is incompatible for multiplication')

def matrix_conversion():
    class NegativeInputError(Exception):
        pass   
    try:  
        i=int(input('Rows: '))
        j=int(input('Columns: '))
        if i<1 and j<1:
            raise NegativeInputError
        A= [["_" for _ in range(j)] for _ in range(i)]
        for r_index in range(i):
            for c_index in range(j):
                A[r_index][c_index] = int(input('Enter element : '))
    except NegativeInputError:
        print('Please enter positive integer values for the rows and columns')
    except ValueError:
        print('Please enter integer values for the rows and columns')
    except Exception:
        print('Please enter valid inputs')


    A_T=[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    print(A_T)
    
