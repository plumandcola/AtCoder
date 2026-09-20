#99点解法
n = int(input())
k = int(input())

ans = [0] * (n+1) #ans[k][i] := 1 ≤ a_1 ≤ ... ≤ a_k ≤ i を満たす整数の組aの個数(累積和) → 二次元を一次元にしたもの
ans[1] = 1
for _ in range(k+1):
    for i in range(n):
        ans[i+1] = (ans[i+1] + ans[i]) % 1000000007

print(ans[n])