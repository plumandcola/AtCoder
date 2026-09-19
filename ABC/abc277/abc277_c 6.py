from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.parents[1] #1階を追加
        """各要素の親要素の番号を格納するdict、要素が根（ルート）の場合は-(そのグループの要素数)を格納する"""
    
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


N = int(input())

uf = UnionFind()
g = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    uf.union(A, B)

ans = 1
for f in uf.parents:
    if uf.same(1, f):
        ans = max(ans, f)

print(ans)