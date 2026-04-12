from collections import defaultdict
import heapq

count = defaultdict(int)
max_q = [] #最大値から取り出すため、格納する数字は正負を逆転させる
min_q = []

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        while count[min_q[0]] == 0:
            heapq.heappop(min_q)
        while count[-max_q[0]] == 0:
            heapq.heappop(max_q)
        print(- max_q[0] - min_q[0])
        continue
    
    x = query[1]
    if query[0] == 1:
        count[x] += 1
        heapq.heappush(min_q, x)
        heapq.heappush(max_q, -x)
    elif query[0] == 2:
        c = query[2]
        count[x] = max(0, count[x] - c)
