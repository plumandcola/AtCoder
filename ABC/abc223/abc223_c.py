import bisect

N = int(input())

A = [0] * N
B = [0] * N
t = [0.0] * (N+1)
s = [0] * (N+1)
for i in range(N):
    A[i], B[i] = map(int, input().split())
    t[i+1] = t[i] + A[i] / B[i]
    s[i+1] = s[i] + A[i]

i = bisect.bisect_left(t, t[N] / 2)

print(s[i-1] + B[i-1] * (t[N] / 2 - t[i-1]))