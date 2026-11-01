#50点解法
N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(N-K+1):
    for j in range(K):
        ans += a[i+j]

print(ans)