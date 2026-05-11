import math

class SegmentTree:
    def __init__(self, A: list[int]):
        self.N = len(A)
        self.n = (self.N-1).bit_length()
        self.SegmentTree = [0] * (1 << (self.n + 1))
        self.SegmentTree[1 << self.n : (1 << self.n) + self.N] = A[:]
        for pos in range((1 << self.n) - 1, 0, -1):
            self.SegmentTree[pos] = math.gcd(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])

    def query(self, l: int, r: int) -> int:
        l += 1 << self.n
        r += 1 << self.n
        value_l = 0
        value_r = 0
        while l != r:
            if l & 1 == 1:
                value_l = math.gcd(value_l, self.SegmentTree[l])
                l += 1
            if r & 1 == 1:
                r -= 1
                value_r = math.gcd(value_r, self.SegmentTree[r])
            l >>= 1
            r >>= 1
        return math.gcd(value_l, value_r)


N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_SegmentTree = SegmentTree([abs(A[i+1] - A[i]) for i in range(N-1)]) #差を考える
B_SegmentTree = SegmentTree([abs(B[i+1] - B[i]) for i in range(N-1)])

for _ in range(Q):
    h_1, h_2, w_1, w_2 = map(int, input().split())
    print(math.gcd(A[h_1 - 1] + B[w_1 - 1], A_SegmentTree.query(h_1 - 1, h_2 - 1), B_SegmentTree.query(w_1 - 1, w_2 - 1)))
    #考える差の数は、行や列の数よりも1少ないので、queryの引数に注意
