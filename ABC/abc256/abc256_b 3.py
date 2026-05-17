N = int(input())
A = list(map(int, input().split()))

P = N
s = [0] * (N+1)
for i in range(N-1, max(-1, N-4), -1):
    s[i] = s[i+1] + A[i]
    if s[i] < 4:
        P -= 1

print(P)