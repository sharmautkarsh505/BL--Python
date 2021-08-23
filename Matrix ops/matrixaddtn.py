"""
Author:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Date: 2021-08-23 22:20:00
Last Modified by:Utkarsh Sharma(sharmautkarsh2396@gmail.com)
Last Modified time:2021-08-24 00:11:00
Title : Matrix Addition
"""

#incase of square matrix
matrix_1=[[1,2],[3,4]]
matrix_2=[[5,6],[7,8]]

add_result=[[0,0],[0,0]]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        add_result[i][j]=matrix_1[i][j]+matrix_2[i][j]
print(add_result)

#by list comprehension 
add_result_listc=[[matrix_1[i][j]+matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print(add_result_listc)

#incase of rectangular matrix 3x5
matrix_3=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
matrix_4=[[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]

add_result_1=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
#iterate through 3 rows
for i in range(len(matrix_3)):
    #iterate through the 5 columns
    for j in range(len(matrix_3[0])):
        add_result_1[i][j]=matrix_3[i][j]+matrix_4[i][j]
print(add_result_1)

#by list comprehension

add_result_1_listc=[[matrix_3[i][j]+matrix_4[i][j] for j in range(len(matrix_3[0]))] for i in range(len(matrix_3))]
print(add_result_1_listc)


#for 3d square matrix 2x2x2
matrix5=[[[1,2],[3,4]],[[5,6],[7,8]]]
matrix6=[[[9,10],[11,12]],[[13,14],[15,16]]]

add_matrix3=[[[0,0],[0,0]],[[0,0],[0,0]]]

for i in range(len(matrix5)):
    for j in range(len(matrix5[0])):
        for k in range(len(matrix5[0][0])):
            add_matrix3[i][j][k]=matrix5[i][j][k]+matrix6[i][j][k]

print(add_matrix3)

#using list comprehension
add_matrix3_listc=[[[matrix6[i][j][k]+matrix5[i][j][k] for k in range(len(matrix5[0][0]))] for j in range(len(matrix5[0]))] for i in range(len(matrix5))]
print(add_matrix3_listc)