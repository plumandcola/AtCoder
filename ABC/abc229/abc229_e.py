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

    def union(self, x: int, y: int) -> int:
        """要素xが属するグループと要素yが属するグループとを併合する"""
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return ans_i
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x

        return ans_i - 1


N, M = map(int, input().split())

g = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A-1].append(B-1)

uf = UnionFind(N)

ans = [0] #何もないところに、頂点N-1から逆順に1まで追加していく
ans_i = 0
for i in range(N-1, 0, -1):
    ans_i += 1

    for j in g[i]:
        ans_i = uf.union(i, j)
    
    ans.append(ans_i)

print(*ans[::-1], sep = "\n")
