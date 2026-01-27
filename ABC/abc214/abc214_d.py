import heapq

def find(x: int) -> int:
    """要素xが属するグループの根を返す"""
    if parents[x] < 0: #根
        return x
    else:
        parents[x] = find(parents[x]) #経路圧縮
        return parents[x]

def union(x: int, y: int):
    """要素xが属するグループと要素yが属するグループとを併合する"""
    x = find(x)
    y = find(y)
    
    if x == y:
        return
    
    if parents[x] > parents[y]:
        x, y = y, x
    
    parents[x] += parents[y]
    parents[y] = x

def size(x: int) -> int:
    """要素xが属するグループのサイズ（要素数）を返す"""
    return -parents[find(x)]


N = int(input())

edges = []
for _ in range(N-1):
    u, v, w = map(int, input().split())
    heapq.heappush(edges, (w, u-1, v-1))

ans = 0
parents = [-1] * N
"""各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""
for _ in range(N-1):
    w, u, v = heapq.heappop(edges)
    ans += w * (size(u) * size(v))
    union(u, v)

print(ans)