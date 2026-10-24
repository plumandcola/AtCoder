#100点解法
W, H = map(int, input().split())
mod = 1000000007

ans = [[1] * W for _ in range(H)]

for i in range(1, H):
    for j in range(1, W):
        ans[i][j] = (ans[i-1][j] + ans[i][j-1]) % mod

print(ans[H-1][W-1])