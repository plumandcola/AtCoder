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


S = input()

ans = [[0], [int(S[0])], [1]]
for i in range(1, len(S)):
    ans = matrix_product([[2, 1, 0], [0, 10, 2 * int(S[i])], [0, 0, 2]], ans)
ans = matrix_product([[1, 1, 0]], ans)

print(ans[0][0])