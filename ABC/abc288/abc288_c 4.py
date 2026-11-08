class UnionFind:
    def __init__(self, n: int):
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


ans = 0
N, M = map(int, input().split())
uf = UnionFind(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    if uf.same(A, B):
        ans += 1
    else:
        uf.union(A, B)

print(ans)