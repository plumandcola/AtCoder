class SegmentTree:
    def __init__(self, A: list[int], func, ide_ele):
        self.N = len(A)
        self.n = (self.N-1).bit_length()
        self.ide_ele = ide_ele
        self.SegmentTree = [self.ide_ele] * (1 << (self.n + 1))
        self.SegmentTree[1 << self.n : (1 << self.n) + self.N] = A[:]
        self.func = func
        for pos in range((1 << self.n) - 1, 0, -1):
            self.SegmentTree[pos] = self.func(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])

    def update(self, pos: int, x: int):
        """pos (0 ≤ pos < N)番目の値をxに更新"""
        pos += 1 << self.n
        self.SegmentTree[pos] = x
        pos >>= 1
        while pos > 0:
            self.SegmentTree[pos] = self.func(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])
            pos >>= 1
    
    def add(self, pos: int, x: int):
        """pos (0 ≤ pos < N)番目の値にxを足す"""
        pos += 1 << self.n
        self.SegmentTree[pos] += x
        pos >>= 1
        while pos > 0:
            self.SegmentTree[pos] = self.func(self.SegmentTree[pos << 1], self.SegmentTree[pos << 1 | 1])
            pos >>= 1
    
    def query(self, l: int, r: int) -> int:
        """[l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のfuncを求める"""
        l += 1 << self.n
        r += 1 << self.n
        value_l = self.ide_ele
        value_r = self.ide_ele
        while l != r:
            if l & 1 == 1:
                value_l = self.func(value_l, self.SegmentTree[l])
                l += 1
            if r & 1 == 1:
                r -= 1
                value_r = self.func(value_r, self.SegmentTree[r])
            l >>= 1
            r >>= 1
        return self.func(value_l, value_r)

def add(a: int, b: int) -> int:
    return a + b


N = int(input())
S = [ord(c) - ord('a') for c in input()]

is_sorted = SegmentTree([int(S[i] <= S[i+1]) for i in range(N-1)], add, 0)
st_min = SegmentTree(S, min, float("inf"))
st_max = SegmentTree(S, max, -float("inf"))
count = [SegmentTree([int(S[i] == j) for i in range(N)], add, 0) for j in range(26)]

Q = int(input())
for _ in range(Q):
    query = input().split()
    match int(query[0]):
        case 1:
            x = int(query[1]) - 1
            c = ord(query[2]) - ord('a')

            count[S[x]].add(x, -1)

            S[x] = c

            if x > 0:
                is_sorted.update(x-1, int(S[x-1] <= S[x]))
            if x < N-1:
                is_sorted.update(x, int(S[x] <= S[x+1]))
            
            st_min.update(x, c)
            st_max.update(x, c)
            count[c].add(x, 1)
        case 2:
            l = int(query[1]) - 1
            r = int(query[2]) - 1

            ans = "Yes"
            if is_sorted.query(l, r) != r - l: ans = "No" #Sのl文字目からr文字目が昇順になっていなければ、Tの部分文字列になり得ない
            for i in range(st_min.query(l, r+1) + 1, st_max.query(l, r+1)):
                if count[i].query(l, r+1) < count[i].query(0, N): ans = "No"
            
            print(ans)
