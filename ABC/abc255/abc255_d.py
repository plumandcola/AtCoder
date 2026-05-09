import bisect

N, Q = map(int, input().split())
A = sorted(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

for _ in range(Q):
    X = int(input())
    i = bisect.bisect_left(A, X)
    print(s[N] - s[i] - X * (N-i) + X * i - s[i])
