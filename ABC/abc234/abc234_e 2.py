import heapq

X = int(input())

q = []
for n in range(1, 10):
    for d in range(-9, 10):
        heapq.heappush(q, (n, d))

while True:
    n, d = heapq.heappop(q)
    if n >= X:
        print(n)
        break

    if 0 <= n % 10 + d <= 9:
        heapq.heappush(q, (10 * n + n % 10 + d, d))