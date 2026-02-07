import heapq

N, M = map(int, input().split())

g1 = [set() for _ in range(N)]
"""g1[b] := bよりも先に現れなければならないa"""
g2 = [set() for _ in range(N)]
"""g2[a] := aが先に現れなければならないb"""
for _ in range(M):
    A, B = map(int, input().split())
    g1[B-1].add(A-1)
    g2[A-1].add(B-1)

q = [] #Pに追加できる数字
for i in range(N):
    if len(g1[i]) == 0:
        heapq.heappush(q, i)

ans = []
while q:
    a = heapq.heappop(q)
    ans.append(a + 1)
    for b in g2[a]:
        g1[b].remove(a)
        if len(g1[b]) == 0: #bをPに追加できるようになったら
            heapq.heappush(q, b)

if len(ans) == N: #すべての数字をPに追加できたら
    print(*ans)
else:
    print(-1)