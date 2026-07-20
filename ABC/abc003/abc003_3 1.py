N, K = map(int, input().split())
R = sorted(map(int, input().split()), reverse=True)

ans = 0
for i in range(K):
    ans += R[i] * (1/2) ** (i+1)

print(ans)