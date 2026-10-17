#20点解法
N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
else:
    ans = 0
    for l in range(N):
        for r in range(l, N):
            p = 1
            for i in range(l, r + 1):
                p *= s[i]
                if p > K:
                    break
            else:
                ans = max(ans, r - l + 1)

    print(ans)
