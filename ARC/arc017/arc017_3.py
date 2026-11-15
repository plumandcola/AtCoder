from collections import defaultdict

N, X = map(int, input().split())
w = [int(input()) for _ in range(N)]

l = N - N//2
r = N//2
count_l = defaultdict(int)
for b in range(1 << l):
    s = 0
    for i in range(l):
        if (b >> i) & 1:
            s += w[i]
    count_l[s] += 1

count_r = defaultdict(int)
for b in range(1 << r):
    s = 0
    for i in range(r):
        if (b >> i) & 1:
            s += w[l + i]
    count_r[s] += 1

ans = 0
for s in count_l:
    ans += count_l[s] * count_r[X - s]

print(ans)