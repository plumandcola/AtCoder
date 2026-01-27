import heapq

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

q = []
for i in range(N):
    heapq.heappush(q, (T[i], i))

ans = [float("inf")] * N
while q:
    t, i = heapq.heappop(q)
    if ans[i] == float("inf"):
        ans[i] = t
        heapq.heappush(q, (t + S[i], (i+1) % N))

print(*ans, sep = "\n")