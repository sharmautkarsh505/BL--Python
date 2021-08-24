"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 12:35:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-24 12:48:00
Title : Inverse of a 2x2 matrix
"""

A=[[3,1],[4,2]]

A_=[[3,1],[4,2]]
detA=abs((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))
A_[0][0],A_[1][1]=A_[1][1],A_[0][0]
A_[0][1]=-A_[0][1]
A_[1][0]=-A_[1][0]

invA=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(A_[0])):
        invA[i][j]=(1/detA)*A_[i][j]

print(invA)

#proof inverse is legit 
#AxinvA will be equal to identity matrix
I=[[0,0],[0,0]]
for i in range(len(A)):
    for j in range(len(invA[0])):
        for k in range(len(invA)):
            I[i][j]+=A[i][k]*invA[k][j]
            if I==[[1,0],[0,1]]:
                print('invA is the inverse of A')