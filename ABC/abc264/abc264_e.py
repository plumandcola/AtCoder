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
        
        if x < y: #ここはテンプレートと違う、親はなるべくNにする
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        """要素xが属するグループのサイズ（要素数）を返す"""
        return - self.parents[self.find(x)]


N, M, E = map(int, input().split())

U = [0] * E
V = [0] * E
for i in range(E):
    U[i], V[i] = map(int, input().split())
    U[i] = min(U[i] - 1, N)
    V[i] = min(V[i] - 1, N)

Q = int(input())
X = [int(input()) for _ in range(Q)]

usable = [True] * E #電線を辿ることができるか
for i in range(Q):
    usable[X[i] - 1] = False

uf = UnionFind(N+1)

for i in range(E):
    if usable[i] == True:
        uf.union(U[i], V[i])

ans = []
#クエリを逆順に処理
for i in range(Q-1, -1, -1):
    ans.append(uf.size(N) - 1)
    uf.union(U[X[i] - 1], V[X[i] - 1])

print(*ans[::-1], sep="\n")