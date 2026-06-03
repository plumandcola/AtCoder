class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        """各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""
    
    def find(self, x: int) -> int:
        """要素xが属するグループの根を返す"""
        if self.parents[x] < 0: #根
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) #経路圧縮
            return self.parents[x]

    def union(self, x: int, y: int):
        """要素xが属するグループと要素yが属するグループとを併合する"""
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x: int, y: int) -> bool:
        """要素x, yが同じグループに属するかどうかを返す"""
        return self.find(x) == self.find(y)


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
uf = UnionFind(N)
for c, i, a, b in edges:
    if i == -1:
        uf.union(a, b)
    else:
        ans[i] = not uf.same(a, b)

for i in range(Q):
    print("Yes" if ans[i] else "No")
