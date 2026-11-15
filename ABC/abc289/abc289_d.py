N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [False] * (X+1)
dp[0] = True
j = 0 #Bのインデックス
for i in range(X):
    if j < M and B[j] == i:
        j += 1
        continue

    if dp[i] == False: continue

    for a in A:
        if i+a > X: break

        dp[i+a] = True

print("Yes" if dp[X] else "No")