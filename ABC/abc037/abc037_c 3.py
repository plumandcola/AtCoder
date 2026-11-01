#100点解法
N, K = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a[:K])
ans = s
for i in range(N-K):
    s -= a[i]
    s += a[i+K]
    ans += s

print(ans)