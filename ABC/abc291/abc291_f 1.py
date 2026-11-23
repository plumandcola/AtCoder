N, M = map(int, input().split())
S = [input() for _ in range(N)]


from_1 = [float("inf")] * N
from_1[0] = 0
for i in range(N-1):
    for j in range(M):
        if S[i][j] == '1':
            from_1[i+j+1] = min(from_1[i+j+1], from_1[i] + 1)

to_N = [float("inf")] * N
to_N[N-1] = 0
for i in range(N-2, -1, -1):
    for j in range(M):
        if S[i][j] == '1':
            to_N[i] = min(to_N[i], to_N[i+j+1] + 1)


ans = [float("inf")] * (N-2)
for k in range(1, N-1):
    for i in range(max(0, k-M+1), k):
        for j in range(M):
            if S[i][j] == '1' and i+j+1 > k:
                ans[k-1] = min(ans[k-1], from_1[i] + 1 + to_N[i+j+1])
    if ans[k-1] == float("inf"):
        ans[k-1] = -1

print(*ans)