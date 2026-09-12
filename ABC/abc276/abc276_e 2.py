from collections import deque

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


H, W = map(int, input().split())
C = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if C[i][j] == 'S':
            y = i
            x = j

ans = "No"
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
for dy, dx in moves:
    if not 0 <= y+dy < H or not 0 <= x+dx < W or C[y+dy][x+dx] != '.': continue

    uf = UnionFind(H*W)
    q = deque([(y+dy, x+dx)])
    while q:
        i, j = q.popleft()
        for di, dj in moves:
            if not 0 <= i+di < H or not 0 <= j+dj < W or C[i+di][j+dj] != '.': continue
            if uf.same(i * W + j, (i+di) * W + (j+dj)): continue

            uf.union(i * W + j, (i+di) * W + (j+dj))
            q.append((i+di, j+dj))
    
    for di, dj in moves:
        if (dy == di and dx == dj) or not 0 <= y+di < H or not 0 <= x+dj < W: continue

        if uf.same((y+dy) * W + (x+dx), (y+di) * W + (x+dj)):
            ans = "Yes"

print(ans)