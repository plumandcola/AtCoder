#100点解法
class LCA:
    def __init__(self, g: list[list[int]]):
        self.N = len(g)
        self.n = (self.N - 1).bit_length()
        self.parent = [[0] * self.N for _ in range(self.n)]
        self.dist = [-1] * self.N
        self.dist[0] = 0
        q = [0]
        while q:
            v = q.pop()
            for u in g[v]:
                if self.dist[u] == -1:
                    self.parent[0][u] = v
                    self.dist[u] = self.dist[v] + 1
                    q.append(u)
        
        for k in range(self.n - 1):
            for i in range(self.N):
                self.parent[k+1][i] = self.parent[k][self.parent[k][i]]

    def query(self, v: int, u: int) -> int:
        #vの方が深くなるようにする
        if self.dist[v] < self.dist[u]:
            v, u = u, v

        #LCAまでの距離を同じにする
        diff = self.dist[v] - self.dist[u]
        k = 0
        while diff:
            if diff & 1:
                v = self.parent[k][v]
            diff >>= 1
            k += 1

        #二分探索でLCAを求める
        if v == u: return v
        for k in range(self.n - 1, -1, -1):
            if self.parent[k][v] != self.parent[k][u]:
                v = self.parent[k][v]
                u = self.parent[k][u]
        return self.parent[0][v]

    def get_dist(self, v: int, u: int) -> int:
        return self.dist[v] + self.dist[u] - 2 * self.dist[self.query(v, u)]


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)

tree = LCA(g)

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(tree.get_dist(a-1, b-1) + 1)
