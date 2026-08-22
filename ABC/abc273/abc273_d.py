import bisect
from collections import defaultdict

H, W, r_s, c_s = map(int, input().split())

rows = defaultdict(list)
columns = defaultdict(list)

N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    rows[r].append(c)
    columns[c].append(r)

for r in rows:
    rows[r].sort()
for c in columns:
    columns[c].sort()

R = r_s
C = c_s
Q = int(input())
for _ in range(Q):
    d, l = input().split()
    l = int(l)
    
    if d == 'L':
        i = bisect.bisect_left(rows[R], C)
        C = max(1, C - l)
        if i > 0:
            C = max(C, rows[R][i-1] + 1)
    elif d == 'R':
        i = bisect.bisect_left(rows[R], C)
        C = min(W, C + l)
        if i < len(rows[R]):
            C = min(C, rows[R][i] - 1)
    elif d == 'U':
        i = bisect.bisect_left(columns[C], R)
        R = max(1, R - l)
        if i > 0:
            R = max(R, columns[C][i-1] + 1)
    elif d == 'D':
        i = bisect.bisect_left(columns[C], R)
        R = min(H, R + l)
        if i < len(columns[C]):
            R = min(R, columns[C][i] - 1)
    
    print(R, C)
