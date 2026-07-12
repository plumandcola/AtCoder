class BIT():
    def __init__(self, n: int): #BITの作成
        self.Tree = [0] * (n+1) #0で初期化
        self.n = n
    
    def add(self, i: int, x: int): #A[i]にxを足す
        while i <= self.n:
            self.Tree[i] += x
            i += i & -i
    
    def sum(self, i: int) -> int: #A[i]までの累積和を計算
        ans = 0
        while i > 0:
            ans += self.Tree[i]
            i -= i & -i
        return ans


n = 7
S = input()
T = "atcoder"

bit = BIT(n)
atc = {c: i for i, c in enumerate("atcoder")}
a = [atc[S[i]] for i in range(n)]

res = 0
for i in range(n):
    res += (i - bit.sum(a[i]))
    bit.add(a[i] + 1, 1)

print(res)