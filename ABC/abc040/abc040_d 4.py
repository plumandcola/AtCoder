#100点解法
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

    def size(self, x: int) -> int:
        """要素xが属するグループのサイズ（要素数）を返す"""
        return - self.parents[self.find(x)]


q = []

N, M = map(int, input().split())
for _ in range(M):
    a, b, y = map(int, input().split())
    q.append([y, -1, a-1, b-1]) #-1は、クエリでないことを表す

Q = int(input())
for i in range(Q):
    v, w = map(int, input().split())
    q.append([w, i, v-1, -1])

q.sort(reverse=True) #年の降順にソート

ans = [0] * Q
uf = UnionFind(N)

for query in q:
    if query[1] == -1: #道路を使えるようにする
        a = query[2]
        b = query[3]
        uf.union(a, b)
    else: #クエリ
        i = query[1]
        v = query[2]
        ans[i] = uf.size(v)

print(*ans, sep="\n")