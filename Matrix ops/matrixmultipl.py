"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 00:09:00
Last Modified by:----
Last Modified time:----
Title : Matrix Multiplication
"""
#for square matrices
matrix1=[[1,2],[3,4]]
matrix2=[[5,6],[7,8]]

multiply_result=[[0,0],[0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            multiply_result[i][j]+=matrix1[i][k]*matrix2[k][j]

print(multiply_result)

#for rectangular matrices
#3x2 matrix
A=[[1,2],[3,4],[5,6]]
#2x3 matrix
B=[[7,8,9],[10,11,12]]
#3x3 matrix
m_result=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            m_result[i][j]+=A[i][k]*B[k][j]

print(m_result)
