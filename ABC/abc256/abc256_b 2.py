N = int(input())
A = list(map(int, input().split()))

P = 0
s = [0] * (N+1)
for i in range(N-1, -1, -1):
    s[i] = s[i+1] + A[i]
    if s[i] >= 4:
        P += 1

print(P)