from collections import deque

first, last = input().split()
N = int(input())
s = set(input() for _ in range(N))

if first == last:
    print(0)
    print(first)
    print(last)
else:
    q = deque([last])
    cur = last
    dist = {cur: 0}
    before = {}
    while q:
        cur = q.popleft()
        for i in range(len(cur)):
            for j in range(26):
                c = chr(ord('a') + j)
                next = cur[:i] + c + cur[i+1:]
                if next not in dist and (next in s or next == first):
                    dist[next] = dist[cur] + 1
                    before[next] = cur
                    q.append(next)

    if first in dist:
        ans = []
        cur = first
        while cur != last:
            ans.append(cur)
            cur = before[cur]
        print(len(ans) - 1)
        print(*ans, sep="\n")
        print(last)
    else:
        print(-1)
