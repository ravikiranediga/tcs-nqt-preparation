A=[[1,2],
   
[3,4]

]
B=[
    [5,6],

[7,8]

]
result =[ [ 0,0],
      [0,0]]

for i in range(2):
    for  j  in range(2):

        result[i][j]=A[i][j]+B[i][j]

for row in result:
    print(row)


#Complexity 
#T:O(n^2)
#S:O(n^2)
