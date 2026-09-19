N, M = map(int, input().split())
A = sorted(map(int, input().split()))

A *= 2 #2周期用意する

s = [0] * (2*N + 1) #累積和
for i in range(2*N):
    s[i+1] = s[i] + A[i]

ans = 0 #テーブルの上に置いたカードの総和の最大値
r = 0
for l in range(N):
    r = max(r, l) #もし前回でl==rとなってしまった時のため
    while r+1 < l+N and (A[r+1] == A[r] or A[r+1] == (A[r] + 1) % M): #1周期を超えないようにしつつ右端を伸ばす
        r += 1
    
    ans = max(ans, s[r+1] - s[l])

print(s[N] - ans) #カードの総合計から、テーブルの上に置いたカードの総和の最大値を引く