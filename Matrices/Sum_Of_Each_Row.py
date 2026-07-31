matrix=[ 
    [1,2,3],
    [3,4,5],
    [6,7,8]

]


for row in matrix:
    total=0

    for num in row:
        total+=num
    print(total)


#Complexity 
#T:O(n^m)
#S:O(1)
