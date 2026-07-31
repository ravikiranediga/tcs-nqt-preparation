matrix=[ 
    [1,2,3],
    [2,4,5],
    [3,5,8]

]

flag=True
for i in range(len(matrix)):
    for j in range(len(matrix)):

        if matrix[i][j]!=matrix[j][i]:
            flag=False
if flag:
    print("Symmetric")
else:
    print("Not Symmetric")


#Complexity
#Time  : O(n²)
#Space : O(1)