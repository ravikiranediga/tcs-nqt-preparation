matrix=[ 
    [1,2,3],
    [3,4,5],
    [6,7,8]

]

rows=len(matrix)
cols=len(matrix[0])

for j in range(cols):
    total=0
    for i in range(rows):
        total+=matrix[i][j]

    print(total)

#Complexity 
#T:O(n^m)
#S:O(1)


