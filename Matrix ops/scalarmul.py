"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 11:14:00
Last Modified by:----
Last Modified time:----
Title : Scalar multiplication
"""
A=[[1,1],[1,1]]

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j]=2*A[i][j]

print(A)