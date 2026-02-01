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


N, M = map(int, input().split())

s = 0 #辺の長さの和
edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A-1, B-1))
    if C > 0:
        s += C

edges.sort()

parents = [-1] * N
"""各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""
for C, A, B in edges:
    if not same(A, B):
        union(A, B)
        if C > 0:
            s -= C

print(s)