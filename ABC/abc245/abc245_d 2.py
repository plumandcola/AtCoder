N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = C[N:]
for i in range(M, -1, -1):
    for j in range(M-i):
        if 0 <= N-M+i+j < N:
            B[i] -= A[N-M+i+j] * B[M-j]
    B[i] //= A[N]

print(*B)