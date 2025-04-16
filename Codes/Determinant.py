def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        submatrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(submatrix)
    
    return det


n = int(input())
matrix = []

for l in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


print(determinant(matrix))
