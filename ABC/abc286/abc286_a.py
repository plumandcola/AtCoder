N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * N
for i in range(P-1):
    B[i] = A[i]
for i in range(Q-P+1):
    B[P+i-1] = A[R+i-1]
for i in range(Q, R-1):
    B[i] = A[i]
for i in range(S-R+1):
    B[R+i-1] = A[P+i-1]
for i in range(S, N):
    B[i] = A[i]

print(*B)