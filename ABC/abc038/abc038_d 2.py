#100点解法
class BIT:
    def __init__(self, n: int): #BITの作成
        self.Tree = [0] * (n+1) #0で初期化
        self.n = n
    
    def update(self, i: int, x: int): #A[i]をxに更新する
        while i <= self.n:
            self.Tree[i] = max(self.Tree[i], x)
            i += i & -i
    
    def query(self, i: int) -> int: #A[i]までの最大値を計算
        ans = 0
        while i > 0:
            ans = max(ans, self.Tree[i])
            i -= i & -i
        return ans


N = int(input())
boxes = [] #wの昇順かつhの降順でソート
for _ in range(N):
    w, h = map(int, input().split())
    boxes.append((w, -h))
boxes.sort()

dp = [0] * 100001 #dp[h] := 最も外側の箱の縦がh cmのときに、最大で何重の入れ子にできるか
bit = BIT(100001)
for w, h in boxes:
    h *= -1 #hの符号を反転させているので、元に戻す
    dp[h] = max(dp[h], bit.query(h-1) + 1)
    bit.update(h, dp[h])

print(max(dp))