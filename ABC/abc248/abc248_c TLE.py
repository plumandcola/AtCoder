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


N, M, K = map(int, input().split())

ans = [[0] for _ in range(K+1)]
ans[0][0] = 1
transformation_matrix = [[1 if 1 <= i-j <= M else 0 for j in range(K+1)] for i in range(K+1)]

while N:
    if N & 1 == 1:
        ans = matrix_product(transformation_matrix, ans)
    transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
    N >>= 1

print(sum(ans[i][0] for i in range(K+1)) % 998244353)