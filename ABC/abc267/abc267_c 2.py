N, M = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

ans_i = sum((i+1) * A[i] for i in range(M))
ans = ans_i
for i in range(N - M):
    ans_i += - (s[i+M] - s[i]) + M * A[i+M]
    ans = max(ans, ans_i)

print(ans)