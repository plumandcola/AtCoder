from collections import deque

cylinder = deque()

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        c = query[2]
        cylinder.append([x, c])
    elif query[0] == 2:
        c = query[1]
        s = 0
        while c > 0:
            if cylinder[0][1] <= c:
                s += cylinder[0][0] * cylinder[0][1]
                c -= cylinder[0][1]
                cylinder.popleft()
            else:
                s += cylinder[0][0] * c
                cylinder[0][1] -= c
                c = 0
        print(s)