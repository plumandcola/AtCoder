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


H, W, K = map(int, input().split())
x_1, y_1, x_2, y_2 = map(int, input().split())

ans = [[0] for _ in range(4)]
b = int(x_1 == x_2) | ((y_1 == y_2) << 1)
ans[b][0] = 1

transformation_matrix = [[H+W-4, H-1, W-1, 0], [1, W-2, 0, W-1], [1, 0, H-2, H-1], [0, 1, 1, 0]]

while K:
    if K & 1 == 1:
        ans = matrix_product(transformation_matrix, ans)
    transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
    K >>= 1

print(ans[3][0])