#30点解法
N, M = map(int, input().split())

l = [0] * N
r = [0] * N
s = [0] * N
for i in range(N):
    l[i], r[i], s[i] = map(int, input().split())

ans = 0
for b in range(1 << N):
    S = 0
    jewels = [False] * M
    for i in range(N):
        if (b >> i) & 1:
            S += s[i]
            for j in range(l[i] - 1, r[i]):
                jewels[j] = True

    for j in range(M):
        if jewels[j] == False: #獲得していない宝石がある
            ans = max(ans, S)
            break

print(ans)