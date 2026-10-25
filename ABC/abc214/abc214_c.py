import heapq

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

#ダイクストラ法
q = []
for i in range(N):
    heapq.heappush(q, (T[i], i))

ans = T[:]
while q:
    t, i = heapq.heappop(q)
    if ans[i] < t: continue

    if ans[(i+1) % N] > t + S[i]:
        heapq.heappush(q, (t + S[i], (i+1) % N))
        ans[(i+1) % N] = t + S[i]

print(*ans, sep = "\n")