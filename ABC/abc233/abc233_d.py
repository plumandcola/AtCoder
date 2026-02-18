from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
count = defaultdict(int)
s = 0
count[s] += 1
for i in range(N):
    s += A[i]
    ans += count[s - K]
    count[s] += 1

print(ans)