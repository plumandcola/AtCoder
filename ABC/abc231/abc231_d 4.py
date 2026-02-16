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

parents = [-1] * N
"""各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""

ans = True
count = [0] * N
for _ in range(M):
    A, B = map(int, input().split())

    count[A-1] += 1
    count[B-1] += 1

    if count[A-1] > 2 or count[B-1] > 2:
        ans = False

    if same(A-1, B-1):
        ans = False
    else:
        union(A-1, B-1)

print("Yes" if ans else "No")