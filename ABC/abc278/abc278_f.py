N = int(input())
S = [input() for _ in range(N)]

g = [[] for _ in range(N)] #g[i] := 整数iを選ばれた後に、選ぶことのできる整数
for i in range(N):
    for j in range(N):
        if S[i][-1] == S[j][0]:
            g[i].append(j)

dp = [[False] * N for _ in range(1 << N)]
"""dp[b][i] := ビット列bで表される集合Sに含まれる全ての整数が選ばれて、最後に整数iを選ばれている状態で、勝つことができるかどうか"""
for b in range((1 << N) - 1, -1, -1):
    for i in range(N):
        if (b >> i) & 1 == 0: continue

        for j in g[i]:
            if (b >> j) & 1 == 1: continue #すでに整数jが選ばれていたら、整数jは選べない

            if dp[b | (1 << j)][j] == False: #整数jを選べば、相手を負けにできる
                dp[b][i] = True

for i in range(N):
    if dp[1 << i][i] == False: #初手で整数iを選べば、相手を負けにできる
        print("First")
        break
else:
    print("Second")
