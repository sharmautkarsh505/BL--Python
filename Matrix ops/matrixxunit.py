"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 11:07:00
Last Modified by:----
Last Modified time:----
Title : Mutiplication with identity matrix
"""

A=[[1,2,3],[4,5,6],[7,8,9]]
I=[[1,0,0],[0,1,0],[0,0,1]]

result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(I[0])):
        for k in range(len(I)):
            result[i][j]+=A[i][k]*I[k][j]
            if result==A:
                print('Hence Proved')

