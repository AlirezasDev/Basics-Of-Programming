def multiply(n, k, m, matrix1, matrix2):
    result = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for l in range(k):
                result[i][j] += matrix1[i][l] * matrix2[l][j]

    return result

n, k, m = map(int, input().split())

matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2 = []
for _ in range(k):
    row = list(map(int, input().split()))
    matrix2.append(row)

result = multiply(n, k, m, matrix1, matrix2)

for row in result:
    print(' '.join(map(str, row)))
