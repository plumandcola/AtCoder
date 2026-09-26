def matrix_product(A, B):
    m = len(A)
    n = len(B)
    l = len(B[0])
    AB = [[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                AB[i][j] = (AB[i][j] + A[i][k] * B[k][j]) % mod
    return AB


N, P = map(int, input().split())
mod = 998244353

inv_100 = pow(100, mod - 2, mod)

ans = [[1], [0], [1]]
transformation_matrix = [[(100 - P) * inv_100 % mod, P * inv_100 % mod, 1], [1, 0, 0], [0, 0, 1]]
N -= 1
while N:
    if N & 1 == 1:
        ans = matrix_product(transformation_matrix, ans)
    transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
    N >>= 1

print(ans[0][0])