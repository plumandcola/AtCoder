cards = list(range(1, 7))

N = int(input())

dp = [[0] * 6 for _ in range(30)] #ダブリング
dp[0] = [2, 3, 4, 5, 6, 1] #操作を5回行った時のカードの順番
n = N // 5 #操作5回を1周期として、何周期か
i = 0 #周期数が2の何乗か
while n:
    if n & 1 == 1:
        for j in range(6):
            cards[j] = dp[i][cards[j] - 1]
    
    for j in range(6):
        dp[i+1][j] = dp[i][dp[i][j] - 1]
    n >>= 1
    i += 1

for i in range(N%5): #1周期に入らなかった操作の分
    cards[i%5], cards[i%5 + 1] = cards[i%5 + 1], cards[i%5]

print(*cards, sep="")