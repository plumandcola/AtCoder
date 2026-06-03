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


N, M = map(int, input().split())

uf = UnionFind(N)

ans = True
count = [0] * N
for _ in range(M):
    A, B = map(int, input().split())

    count[A-1] += 1
    count[B-1] += 1

    if count[A-1] > 2 or count[B-1] > 2:
        ans = False

    if uf.same(A-1, B-1):
        ans = False
    else:
        uf.union(A-1, B-1)

print("Yes" if ans else "No")
