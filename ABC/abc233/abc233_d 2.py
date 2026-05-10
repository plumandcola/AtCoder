from collections import defaultdict
import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + A[i]

indices = defaultdict(list) #indices[s] := A_iまでの和がsになるiの配列
for i in range(N+1):
    indices[s[i]].append(i)

ans = 0
for l in range(N):
    i = bisect.bisect_left(indices[s[l] + K], l + 1)
    ans += len(indices[s[l] + K]) - i

print(ans)