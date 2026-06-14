def matrix_product(A, B):
    m = len(A)
    n = len(B)
    l = len(B[0])
    AB = [[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                AB[i][j] = AB[i][j] + A[i][k] * B[k][j]
    return AB


N, X, Y = map(int, input().split())

jewels = [[1], [0]]
transformation_matrix = [[X+1, 1], [X * Y, Y]]
N -= 1
while N:
    if N & 1 == 1:
        jewels = matrix_product(transformation_matrix, jewels)
    transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
    N >>= 1

print(jewels[1][0])