N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [-float("inf")] * (N+1) #dp[i] := 山にi個の石があるときに取り除ける石の個数の最大値
dp[0] = 0
for i in range(1, N+1):
    for j in range(K):
        if i - A[j] >= 0:
            num = A[j] + ((i - A[j]) - dp[i - A[j]]) #A[j]個取った後の山は残り(i - A[j])個、そのうちdp[i - A[j]]個を相手に取られる
            dp[i] = max(dp[i], num)

print(dp[N])