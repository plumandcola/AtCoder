#100点解法
class SegmentTree:
    def __init__(self, n: int, func, ide_ele):
        self.N = n
        self.n = (self.N - 1).bit_length()
        self.ide_ele = ide_ele
        self.SegmentTree = [self.ide_ele] * (1 << (self.n + 1))
        self.func = func

    def update(self, pos: int, x: tuple):
        """pos (0 ≤ pos < N)番目の値をxに更新"""
        pos += 1 << self.n
        self.SegmentTree[pos] = x
        pos >>= 1
        while pos > 0:
            self.SegmentTree[pos] = self.func(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])
            pos >>= 1

    def query(self) -> float:
        return self.SegmentTree[1][0] + self.SegmentTree[1][1]

def op(x: tuple, y: tuple) -> tuple:
    return (x[0] * y[0], x[1] * y[0] + y[1])


N, M = map(int, input().split())

queries = []
P = []
for _ in range(M):
    query = input().split()
    p = int(query[0])
    queries.append((p, float(query[1]), float(query[2])))
    P.append(p)

#座標圧縮
P_sorted = sorted(set(P))
n = len(P_sorted)
P_dict = {P_sorted[i]: i for i in range(n)}

st = SegmentTree(n, op, (1, 0))

ans_min = 1
ans_max = 1
for p, a, b in queries:
    st.update(P_dict[p], (a, b))

    r = st.query()
    ans_min = min(ans_min, r)
    ans_max = max(ans_max, r)

print(ans_min)
print(ans_max)