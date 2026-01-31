from collections import deque
import heapq

Q = int(input())

q1 = deque([])
q2 = [] #優先度付きキュー
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q1.append(query[1])
    elif query[0] == 2:
        if len(q2) == 0:
            print(q1.popleft())
        else:
            print(heapq.heappop(q2))
    elif query[0] == 3:
        while q1:
            heapq.heappush(q2, q1.popleft())