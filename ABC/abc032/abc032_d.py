import bisect

def solve_1():
    l = {} #前半だけの部分集合について、重さの和をキー、価値の和を値としたdict型(辞書型)
    for b in range(1 << (N//2)):
        s_w = 0
        s_v = 0
        for i in range(N//2):
            if (b >> i) & 1:
                s_w += w[i]
                s_v += v[i]

        if s_w in l:
            l[s_w] = max(l[s_w], s_v)
        else:
            l[s_w] = s_v

    l_sorted = sorted(l)

    #l[s_w]が、前半の部分集合のうち、重さの和がs_w以下である集合の価値の和の最大値、となるようにする
    for i in range(len(l_sorted) - 1):
        l[l_sorted[i+1]] = max(l[l_sorted[i+1]], l[l_sorted[i]])

    ans = 0
    for b in range(1 << (N - N//2)):
        s_w = 0
        s_v = 0
        for i in range(N - N//2):
            if (b >> i) & 1:
                s_w += w[i + N//2]
                s_v += v[i + N//2]

        if s_w > W: continue

        i = bisect.bisect_right(l_sorted, W - s_w) #l_sorted[i] <= W - s_wとなるiの最大値
        s = l[l_sorted[i-1]]
        ans = max(ans, s_v + s)
    print(ans)

def solve_2():
    dp = [0] * (1000*N + 1) #dp[j] := 重さの和がjとなる荷物の集合の、価値の和の最大値
    for i in range(N):
        for j in range(1000*N - w[i], -1, -1):
            dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i])
    print(max(dp[:W+1]))

def solve_3():
    dp = [float("inf")] * (1000*N + 1) #dp[j] := 価値の和がjとなる荷物の集合の、重さの和の最小値
    dp[0] = 0
    for i in range(N):
        for j in range(1000*N - v[i], -1, -1):
            dp[j + v[i]] = min(dp[j + v[i]], dp[j] + w[i])

    for j in range(1000*N, -1, -1):
        if dp[j] <= W:
            print(j)
            break


N, W = map(int, input().split())

v = [0] * N
w = [0] * N
for i in range(N):
    v[i], w[i] = map(int, input().split())

if N <= 30:
    solve_1()
elif all(w[i] <= 1000 for i in range(N)):
    solve_2()
elif all(v[i] <= 1000 for i in range(N)):
    solve_3()
