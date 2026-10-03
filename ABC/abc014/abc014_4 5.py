#100点解法
import sys
sys.setrecursionlimit(50000000)


class SegmentTree:
    def __init__(self, A: list[tuple]):
        self.N = len(A)
        self.n = (self.N - 1).bit_length()
        self.SegmentTree = [(float("inf"), float("inf"))] * (1 << (self.n + 1))
        self.SegmentTree[1 << self.n : (1 << self.n) + self.N] = A[:]
        for pos in range((1 << self.n) - 1, 0, -1):
            self.SegmentTree[pos] = min(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])

    def query(self, l: int, r: int) -> int:
        """[l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のminを求める"""
        l += 1 << self.n
        r += 1 << self.n
        value_l = (float("inf"), float("inf"))
        value_r = (float("inf"), float("inf"))
        while l != r:
            if l & 1 == 1:
                value_l = min(value_l, self.SegmentTree[l])
                l += 1
            if r & 1 == 1:
                r -= 1
                value_r = min(self.SegmentTree[r], value_r)
            l >>= 1
            r >>= 1
        return min(value_l, value_r)


N = int(input())

g = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    g[x-1].append(y-1)
    g[y-1].append(x-1)


l = [0] * N
r = [0] * N
tour = []
depth = [0] * N #根からの深さ

def dfs(v: int, p: int):
    l[v] = len(tour)
    tour.append((depth[v], v))
    for u in g[v]:
        if u == p: continue

        depth[u] = depth[v] + 1
        dfs(u, v)
        tour.append((depth[v], v))
    r[v] = len(tour)

dfs(0, -1)

st = SegmentTree(tour)


Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if l[b] < l[a]: a, b = b, a

    p = st.query(l[a], l[b] + 1)[1]
    print(depth[a] + depth[b] - 2 * depth[p] + 1)
