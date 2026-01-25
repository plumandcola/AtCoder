import heapq

balls = []
add = 0

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(balls, query[1] - add)
    elif query[0] == 2:
        add += query[1]
    elif query[0] == 3:
        print(heapq.heappop(balls) + add)