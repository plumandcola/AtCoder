def dfs(pair: list[bool], B: int):
    i = 0 #まだペアができていない人のうち、最小の人
    while i < 2*N and pair[i] == True:
        i += 1
    
    if i == 2*N: #全員ペアができていたら終了
        fun.append(B)
        return
    
    pair[i] = True
    for j in range(i+1, 2*N):
        if pair[j] == False:
            pair[j] = True
            dfs(pair, A[i][j-i-1] ^ B)
            pair[j] = False #元に戻す
    pair[i] = False #元に戻す


N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N - 1)]

fun = [] #「舞踏会全体の楽しさ」の候補全て
pair = [False] * (2*N) #ペアを作ったかどうか
dfs(pair, 0)

print(max(fun))