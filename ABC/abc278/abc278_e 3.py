from collections import defaultdict

H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

num = defaultdict(list) #num[a] := A[i][j] = aである(i, j)のlist
for i in range(H):
    for j in range(W):
        num[A[i][j]].append((i, j))

s = [[0] * (W-w+2) for _ in range(H-h+2)] #いもす法
for a in num:
    #整数aが書かれた(i, j)が全て塗りつぶされるような[ks, kt) × [ls, lt)を求める
    ks = 0
    ls = 0
    kt = H-h+1
    lt = W-w+1
    for i, j in num[a]:
        ks = max(ks, i-h+1)
        ls = max(ls, j-w+1)
        kt = min(kt, i+1)
        lt = min(lt, j+1)

    if ks < kt and ls < lt: #[ks, kt) × [ls, lt)が空でないなら
        s[ks][ls] += 1
        s[ks][lt] -= 1
        s[kt][ls] -= 1
        s[kt][lt] += 1

#累積の計算
for k in range(H-h+1):
    for l in range(W-w):
        s[k][l+1] += s[k][l]
for k in range(H-h):
    for l in range(W-w+1):
        s[k+1][l] += s[k][l]

for k in range(H-h+1):
    ans = [0] * (W-w+1)
    for l in range(W-w+1):
        ans[l] = len(num) - s[k][l]
    print(*ans)
