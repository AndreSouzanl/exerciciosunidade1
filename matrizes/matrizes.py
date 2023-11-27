
mat = []

mat.append([1,2,3])
mat.append([4,5,6])
mat.append([7,8,9])

#! 0 linha 0 coluna
print(mat[0][0])
print(mat[0][1])
print(mat[0][2])

#! 1 linha 1 coluna
print(mat[1][0])
print(mat[1][1])
print(mat[1][2])

#! 2 linha 2 coluna
print(mat[2][0])
print(mat[2][1])
print(mat[2][2])

for i in range(3):
    for j in range(3):
        print("O elemento da linha", i, "coluna", j, "è:", mat[i][j])