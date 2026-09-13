import bisect

N = int(input())

ans = []
for _ in range(N):
    w = int(input())
    i = bisect.bisect_left(ans, w)
    if i != len(ans):
        ans[i] = w
    else:
        ans.append(w)

print(len(ans))