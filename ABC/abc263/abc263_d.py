N, L, R = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

m = [float("inf")] * (N+1) #m[i] := A_iまでを、そのままかLにした時の、総和の最小値
m[0] = 0
for i in range(N):
    m[i+1] = min(m[i] + A[i], L * (i+1))

ans = float("inf")
for y in range(N+1):
    ans = min(ans, m[N - y] + R * y)

print(ans)