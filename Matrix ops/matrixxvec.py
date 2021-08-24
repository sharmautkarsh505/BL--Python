"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 11:29:00
Last Modified by:----
Last Modified time:----
Title : Matrix Vector multiplication
"""
#3x3 matrix
A=[[1,2,3],[4,5,6],[7,8,9]]
#3x1 matrix
B=[[10],[11],[12]]

resultant=[[0],[0],[0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultant[i][j]+=A[i][k]*B[k][j]

print(resultant)