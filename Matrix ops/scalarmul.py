"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 11:14:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-24 11:24:00
Title : Scalar multiplication
"""
#logic gets much clear once used for rectangular matrix
#for square matrix
A=[[1,1],[1,1]]

for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j]=2*A[i][j]

print(A)

#using list comprehension
s_result=[[A[i][j]*4 for j in range(len(A[0]))] for i in range(len(A))]
print(s_result)

#for rectangular matrix 2x4
B=[[1,2,3,4],[5,6,7,8]]

for i in range(len(B)):
    for j in range(len(B[0])):
        B[i][j]=6*B[i][j]
print(B)

#using list comprehension
r_result=[[B[i][j]*6 for j in range(len(B[0]))] for i in range(len(B))]
print(B)