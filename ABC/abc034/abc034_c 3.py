#100点解法
W, H = map(int, input().split())
mod = 1000000007

c = [[] for _ in range(W+H-1)]
for i in range(W+H-1):
    c[i].append(1)
    for j in range(1, i):
        c[i].append((c[i-1][j-1] + c[i-1][j]) % mod)
    c[i].append(1)

print(c[W+H-2][W-1])