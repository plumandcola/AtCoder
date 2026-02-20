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

def same(x: int, y: int) -> bool:
    """要素x, yが同じグループに属するかどうかを返す"""
    return find(x) == find(y)


N, M, Q = map(int, input().split())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, -1, a-1, b-1)) #-1は、クエリではないことを表す

for i in range(Q):
    u, v, w = map(int, input().split())
    edges.append((w, i, u-1, v-1)) #iは、何番目のクエリかを表す

edges.sort()

ans = [False] * Q
parents = [-1] * N
"""各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""
for c, i, a, b in edges:
    if i == -1:
        union(a, b)
    else:
        ans[i] = not same(a, b)

for i in range(Q):
    print("Yes" if ans[i] else "No")