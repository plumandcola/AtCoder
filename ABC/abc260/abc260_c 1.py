N, X, Y = map(int, input().split())

jewels = [[0] * 2 for _ in range(N)]
jewels[N-1][0] = 1
for i in range(N-1, 0, -1):
    jewels[i-1][0] += jewels[i][0] #レベルnの赤い宝石 -> レベルn−1の赤い宝石1個
    jewels[i][1] += X * jewels[i][0] #レベルnの赤い宝石 -> レベルnの青い宝石X個

    jewels[i-1][0] += jewels[i][1] #レベルnの青い宝石 -> レベルn−1の赤い宝石1個
    jewels[i-1][1] += Y * jewels[i][1] #レベルnの青い宝石 -> レベルn-1の青い宝石Y個

print(jewels[0][1])