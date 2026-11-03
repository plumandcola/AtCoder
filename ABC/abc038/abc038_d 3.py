#100点解法
class SegmentTree:
    def __init__(self, N: int):
        self.N = N
        self.n = (self.N - 1).bit_length()
        self.size = 1 << self.n
        self.tree = [0] * (self.size << 1)

    def update(self, pos: int, x: int):
        """pos (0 ≤ pos < N)番目の値をxに更新"""
        pos += self.size
        self.tree[pos] = x
        pos >>= 1
        while pos > 0:
            self.tree[pos] = max(self.tree[pos << 1], self.tree[pos << 1 | 1])
            pos >>= 1

    def query(self, l: int, r: int) -> int:
        """[l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のmaxを求める"""
        l += self.size
        r += self.size
        value_l = 0
        value_r = 0
        while l != r:
            if l & 1:
                value_l = max(value_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                value_r = max(self.tree[r], value_r)
            l >>= 1
            r >>= 1
        return max(value_l, value_r)


N = int(input())
boxes = [] #wの昇順かつhの降順でソート
for _ in range(N):
    w, h = map(int, input().split())
    boxes.append((w, -h))
boxes.sort()

dp = [0] * 100001 #dp[h] := 最も外側の箱の縦がh cmのときに、最大で何重の入れ子にできるか
st = SegmentTree(100001)
for w, h in boxes:
    h *= -1 #hの符号を反転させているので、元に戻す
    dp[h] = max(dp[h], st.query(0, h) + 1)
    st.update(h, dp[h])

print(max(dp))