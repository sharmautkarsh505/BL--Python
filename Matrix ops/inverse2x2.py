"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 12:35:00
Last Modified by:----
Last Modified time:----
Title : Inverse of a 2x2 matrix
"""

A=[[3,1],[4,2]]

detA=abs((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))
A[0][0],A[1][1]=A[1][1],A[0][0]
A[0][1]=-A[0][1]
A[1][0]=-A[1][0]

invA=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        invA[i][j]=(1/detA)*A[i][j]

print(invA)
