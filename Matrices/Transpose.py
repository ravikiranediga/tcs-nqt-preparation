matrix = [
    [1,2,3],
    [4,5,6]
]


transpose = [
    [0,0],
    [0,0],
    [0,0]
]


for i in range(2):
    for j in range(3):
        transpose[j][i] = matrix[i][j]


for row in transpose:
    print(row)