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


N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_SegmentTree = SegmentTree([abs(A[i+1] - A[i]) for i in range(N-1)], math.gcd, 0) #差を考える
B_SegmentTree = SegmentTree([abs(B[i+1] - B[i]) for i in range(N-1)], math.gcd, 0)

for _ in range(Q):
    h_1, h_2, w_1, w_2 = map(int, input().split())
    print(math.gcd(A[h_1 - 1] + B[w_1 - 1], A_SegmentTree.query(h_1 - 1, h_2 - 1), B_SegmentTree.query(w_1 - 1, w_2 - 1)))
    #考える差の数は、行や列の数よりも1少ないので、queryの引数に注意
