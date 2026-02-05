imos = []

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    imos.append((A, 1))
    imos.append((A + B, -1))

imos.sort()

ans = [0] * (N+1)
s = 0 #ログインしている人数
for i in range(2*N-1):
    s += imos[i][1]
    ans[s] += imos[i+1][0] - imos[i][0]

print(*ans[1:])