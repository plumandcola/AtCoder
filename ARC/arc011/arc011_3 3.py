from collections import defaultdict, deque

first, last = input().split()

if first == last:
    print(0)
    print(first)
    print(last)

else:
    N = int(input())
    s = [input() for _ in range(N)] + [first] + [last]

    l = len(first)

    g = defaultdict(list)
    for i in range(N+2):
        for j in range(l):
            t = s[i][:j] + '*' + s[i][j+1:]
            g[s[i]].append(t)
            g[t].append(s[i])

    q = deque([last])
    d = defaultdict(int)
    d[last] = 0
    while q:
        v = q.popleft()
        for u in g[v]:
            if u not in d:
                d[u] = d[v] + 1
                q.append(u)

    if first in d:
        print(d[first] // 2 - 1)
        v = first
        while True:
            if d[v] % 2 == 0: #"*"が含まれていない時
                print(v)
            for u in g[v]:
                if d[u] == d[v] - 1:
                    v = u
                    break
            else:
                break
    else:
        print(-1)
