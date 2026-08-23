#10点解法
N, M, D = map(int, input().split())
A = list(map(int, input().split()))

amida = list(range(N))
for _ in range(D):
    for i in range(M):
        amida[A[i] - 1], amida[A[i]] = amida[A[i]], amida[A[i] - 1]

ans = [0] * N
for i in range(N):
    ans[amida[i]] = i + 1

print(*ans, sep="\n")