class SegmentTree:
    def __init__(self, N: int):
        self.N = N
        self.n = (self.N-1).bit_length()
        self.SegmentTree = [0] * (1 << (self.n + 1))

    def add(self, pos: int, x: int):
        """pos (0 ≤ pos < N)番目の値にxを足す"""
        pos += 1 << self.n
        self.SegmentTree[pos] += x
        pos >>= 1
        while pos > 0:
            self.SegmentTree[pos] = self.SegmentTree[pos << 1] + self.SegmentTree[pos << 1 | 1]
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        """[l, r) (0 ≤ l < N, 1 ≤ r ≤ N)の和を求める"""
        l += 1 << self.n
        r += 1 << self.n
        value_l = 0
        value_r = 0
        while l != r:
            if l & 1 == 1:
                value_l += self.SegmentTree[l]
                l += 1
            if r & 1 == 1:
                r -= 1
                value_r += self.SegmentTree[r]
            l >>= 1
            r >>= 1
        return value_l + value_r


N = int(input())
mod = 998244353

s = 0
st_count = SegmentTree(200001)
st_sum = SegmentTree(200001)
for i, A in enumerate(map(int, input().split()), 1):
    s += 2 * st_sum.query(A, 200001) #大きい数字でない方がAである場合
    s += A #xもyもAである場合
    s += 2 * st_count.query(0, A) * A #大きい数字がAである場合
    st_sum.add(A, A)
    st_count.add(A, 1)
    print(s * pow(i * i % mod, mod - 2, mod) % mod) #s/(i*i) % mod
