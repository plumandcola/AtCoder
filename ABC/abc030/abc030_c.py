N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
i = 0 #aのインデックス
j = 0 #bのインデックス
t = 0 #時刻
while i < N: #空港Aから乗れる飛行機がまだ残っている間、ループ
    while i < N and a[i] < t: #空港Aから乗れる次の飛行機を探す
        i += 1
    if i < N: #空港Aから乗れる飛行機が、まだ残っている場合
        t = a[i] + X #空港Bに着く時刻
        
        while j < M and b[j] < t: #空港Bから乗れる次の飛行機を探す
            j += 1
        if j < M: #空港Bから乗れる飛行機が、まだ残っている場合
            t = b[j] + Y #空港Aに着く時刻
            ans += 1 #1往復できたので答えに1を足す

print(ans)