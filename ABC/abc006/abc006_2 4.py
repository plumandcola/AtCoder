def matrix_product(A, B):
    m = len(A)
    n = len(B)
    l = len(B[0])
    AB = [[0]*l for _ in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                AB[i][j] = (AB[i][j] + A[i][k] * B[k][j]) % 10007
    return AB


n = int(input())
if n < 3:
    print(0)
else:
    n -= 3
    a = [[1], [0], [0]]
    transformation_matrix = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    while n:
        if n & 1 == 1:
            a = matrix_product(transformation_matrix, a)
        transformation_matrix = matrix_product(transformation_matrix, transformation_matrix)
        n >>= 1
    
    print(a[0][0])