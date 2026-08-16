def matrix_product(A, B):
    m = len(A)
    n = len(B)
    l = len(B[0])
    AB = [[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                AB[i][j] ^= A[i][k] & B[k][j]
    return AB


K, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

if M <= K:
    print(A[M-1])
else:
    ans = [[A[i]] for i in range(K-1, -1, -1)]
    transformation_matrix = [[0] * K for _ in range(K)]
    for j in range(K):
        transformation_matrix[0][j] = C[j]
    for i in range(1, K):
        transformation_matrix[i][i-1] = (1 << 32) - 1

    M -= K

    while M:
        if M & 1 == 1:
            ans = matrix_product(transformation_matrix, ans)
        transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
        M >>= 1

    print(ans[0][0])
