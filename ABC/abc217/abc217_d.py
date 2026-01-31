from sortedcontainers import SortedSet

L, Q = map(int, input().split())

s = SortedSet([0, L])
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        s.add(x)
    elif c == 2:
        i = s.bisect_left(x)
        print(s[i] - s[i-1])