#100点解法
N, K = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + a[i]

print(sum(s[i+K] - s[i] for i in range(N-K+1)))