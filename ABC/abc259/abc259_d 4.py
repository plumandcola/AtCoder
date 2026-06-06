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


N = int(input())

x = [0] * (N+2)
y = [0] * (N+2)
r = [0] * (N+2)

#点(s_x, s_y), (t_x, t_y)を、半径0の円とみなす
x[N], y[N], x[N+1], y[N+1] = map(int, input().split())

for i in range(N):
    x[i], y[i], r[i] = map(int, input().split())

uf = UnionFind(N+2)
for i in range(N+1):
    for j in range(i+1, N+2):
        if (r[i] - r[j]) ** 2 <= (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 <= (r[i] + r[j]) ** 2:
            uf.union(i, j)

print("Yes" if uf.same(N, N+1) else "No")