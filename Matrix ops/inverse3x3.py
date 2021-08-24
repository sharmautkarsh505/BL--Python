"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-24 14:49:00
Last Modified by:----
Last Modified time:----
Title : Inverse of a 3x3 matrix
"""
M=[[1,0,5],[2,1,6],[3,4,0]]

M_of_cofactors=[[0,0,0],[0,0,0],[0,0,0]]

M_of_cofactors[0][0]=(M[1][1]*M[2][2])-(M[2][1]*M[1][2])
M_of_cofactors[0][1]=-((M[1][0]*M[2][2])-(M[2][0]*M[1][2]))
M_of_cofactors[0][2]=(M[1][0]*M[2][1])-(M[1][1]*M[2][0])
M_of_cofactors[1][0]=-((M[0][1]*M[2][2])-(M[2][1]*M[0][2]))
M_of_cofactors[1][1]=(M[0][0]*M[2][2])-(M[2][0]*M[0][2])
M_of_cofactors[1][2]=-((M[0][0]*M[2][1])-(M[2][0]*M[0][1]))
M_of_cofactors[2][0]=(M[0][1]*M[1][2])-(M[1][1]*M[0][2])
M_of_cofactors[2][1]=-((M[0][0]*M[1][2])-(M[1][0]*M[0][2]))
M_of_cofactors[2][2]=(M[0][0]*M[1][1])-(M[1][0]*M[0][1])


detA=(M[0][0]*M_of_cofactors[0][0])+(M[0][1]*M_of_cofactors[0][1])+(M[0][2]*M_of_cofactors[0][2])

Adj_M=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(M_of_cofactors)):
    for j in range(len(M_of_cofactors[0])):
        Adj_M[i][j]=M_of_cofactors[j][i]

invM=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(M_of_cofactors)):
    for j in range(len(M_of_cofactors[0])):
        invM[i][j]=(1/detA)*Adj_M[i][j]

print(invM)
#proof that invA is inverse of A
I=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(M)):
    for j in range(len(invM[0])):
        for k in range(len(invM)):
            I[i][j]+=M[i][k]*invM[k][j]
            if I==[[1,0,0],[0,1,0],[0,0,1]]:
                print('invM is the inverse of matrix M')
                break




        