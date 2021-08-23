"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-23 23:27:00
Last Modified by:----
Last Modified time:----
Title : User Registration problem
"""

#for 2d square matrix 2x2
matrix1=[[51,22],[45,21]]
matrix2=[[23,7],[28,11]]

sub_matrix1=[[0,0],[0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        sub_matrix1[i][j]=matrix1[i][j]-matrix2[i][j]

print(sub_matrix1)

#by list comprehension
sub_matrix1_listc=[[matrix1[i][j]-matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
print(sub_matrix1_listc)

#for 2d rectangular matrix 3x5
matrix3=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
matrix4=[[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]

sub_matrix2=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(len(matrix3)):
    for j in range(len(matrix3[0])):
        sub_matrix2[i][j]=matrix4[i][j]-matrix3[i][j]

print(sub_matrix2)

#using list comprehension 
sub_matrix2_listc=[[matrix4[i][j]-matrix3[i][j] for j in range(len(matrix3[0]))] for i in range(len(matrix3))]
print(sub_matrix2_listc)

#for 3d square matrix 2x2x2
matrix5=[[[1,2],[3,4]],[[5,6],[7,8]]]
matrix6=[[[9,10],[11,12]],[[13,14],[15,16]]]

sub_matrix3=[[[0,0],[0,0]],[[0,0],[0,0]]]

for i in range(len(matrix5)):
    for j in range(len(matrix5[0])):
        for k in range(len(matrix5[0][0])):
            sub_matrix3[i][j][k]=matrix6[i][j][k]-matrix5[i][j][k]

print(sub_matrix3)

#using list comprehension
sub_matrix3_listc=[[[matrix6[i][j][k]-matrix5[i][j][k] for k in range(len(matrix5[0][0]))] for j in range(len(matrix5[0]))] for i in range(len(matrix5))]
print(sub_matrix3_listc)

