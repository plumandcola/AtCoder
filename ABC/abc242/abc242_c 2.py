def matrix_product(A, B):
    m = len(A)
    n = len(B)
    l = len(B[0])
    AB = [[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                AB[i][j] = (AB[i][j] + A[i][k] * B[k][j]) % 998244353
    return AB


N = int(input())

ans = [[1] for _ in range(9)]
transformation_matrix = [[int(abs(i - j) <= 1) for j in range(9)] for i in range(9)]

N -= 1
while N:
    if N & 1 == 1:
        ans = matrix_product(transformation_matrix, ans)
    transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
    N >>= 1

print(sum(sum(ans[i]) for i in range(9)) % 998244353)