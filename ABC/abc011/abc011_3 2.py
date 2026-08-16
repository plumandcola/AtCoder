N = int(input())
NG = {int(input()) for _ in range(3)}

count = 0 #処理を何回行ったか
M = 3 #選べる数字の上限
while N > 0:
    if N in NG: #NがNG数字の場合
        print("NO")
        break

    for i in range(M, 0, -1):
        if max(0, N - i) not in NG:
            N = max(0, N - i)
            count += 1
            break
    else: #行き先が全てNG数字の場合
        print("NO")
        break
else:
    if count <= 100:
        print("YES")
    else:
        print("NO")
