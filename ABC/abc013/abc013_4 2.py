#100点解法
N, M, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * N for _ in range(31)]
for i in range(N):
    dp[0][i] = i

for i in range(M):
    dp[0][A[i] - 1], dp[0][A[i]] = dp[0][A[i]], dp[0][A[i] - 1]

amida = list(range(N))
i = 0
while D:
    if D & 1 == 1:
        amida = [dp[i][amida[j]] for j in range(N)]
    dp[i+1] = [dp[i][dp[i][j]] for j in range(N)]
    D >>= 1
    i += 1

ans = [0] * N
for i in range(N):
    ans[amida[i]] = i + 1

print(*ans, sep="\n")