"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 14:28:00
Last Modified by:----
Last Modified time:----
Title : Transpose of a matrix
"""
#for square matrix 3x3 using for loops
A=[[1,2,3],[4,5,6],[7,8,9]]

A_T=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        A_T[i][j]=A[j][i]
print(A_T)

#using list comprehension
A_T_lc=[[A[j][i] for j in range(len(A[0]))] for i in range(len(A))]
print(A_T_lc)

#for rectangular matrix 2x5
B=[[1,2,3,4,5],[6,7,8,9,10]]

B_T=[[0,0],[0,0],[0,0],[0,0],[0,0]]
for i in range(len(B[0])):
   for j in range(len(B)):
        B_T[i][j]=B[j][i]
print(B_T)

#using list comprehension
B_T_lc=[[B[j][i] for j in range(len(B))] for i in range(len(B[0]))]
print(B_T_lc)
