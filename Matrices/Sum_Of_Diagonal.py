matrix=[ 
    [1,2,3],
    [3,4,5],
    [6,7,8]

]


total=0
for i in range(len(matrix)):
    total+=matrix[i][i]
print(total)