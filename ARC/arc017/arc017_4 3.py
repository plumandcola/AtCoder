#100点解法
import math

class SegmentTree:
    def __init__(self, A: list[int], func, ide_ele):
        self.N = len(A)
        self.n = (self.N - 1).bit_length()
        self.size = 1 << self.n
        self.func = func
        self.ide_ele = ide_ele
        self.tree = [self.ide_ele] * (self.size << 1)
        self.tree[self.size : self.size + self.N] = A[:]
        for pos in range(self.size - 1, 0, -1):
            self.tree[pos] = self.func(self.tree[pos << 1], self.tree[pos << 1 | 1])

    def update(self, pos: int, x: int):
        """pos (0 ≤ pos < N)番目の値をxに更新"""
        pos += self.size
        self.tree[pos] = x
        pos >>= 1
        while pos > 0:
            self.tree[pos] = self.func(self.tree[pos << 1], self.tree[pos << 1 | 1])
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        """[l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のfuncを求める"""
        l += self.size
        r += self.size
        value_l = self.ide_ele
        value_r = self.ide_ele
        while l != r:
            if l & 1:
                value_l = self.func(value_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                value_r = self.func(self.tree[r], value_r)
            l >>= 1
            r >>= 1
        return self.func(value_l, value_r)


N = int(input())
a = [0] + list(map(int, input().split())) + [0]

d = [a[i+1] - a[i] for i in range(N+1)]

st_gcd = SegmentTree(d, math.gcd, 0)
st_sum = SegmentTree(d, lambda x, y: x+y, 0)

M = int(input())
for _ in range(M):
    t, l, r = map(int, input().split())
    if t == 0:
        L = st_sum.query(0, l) #a[l] = d[0] + ... + d[l-1]をいもす法で求める
        print(math.gcd(L, st_gcd.query(l, r))) #L, d[l], ..., d[r-1]のGCDを求める
    else:
        d[l-1] += t
        st_gcd.update(l-1, d[l-1])
        st_sum.update(l-1, d[l-1])

        d[r] -= t
        st_gcd.update(r, d[r])
        st_sum.update(r, d[r])
