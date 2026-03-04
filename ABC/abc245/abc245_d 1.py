N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [0] * (M+1)
for i in range(M+1):
    B[M-i] = C[N+M-i] // A[N]
    for j in range(N+1):
        C[N+M-i-j] -= A[N-j] * B[M-i]

print(*B)