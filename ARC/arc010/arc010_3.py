n, m, Y, Z = map(int, input().split())

colors = {}
p = [0] * m
for i in range(m):
    c, p_i = input().split()
    colors[c] = i
    p[i] = int(p_i)

b = input()

dp = [[-float("inf")] * m for bit in range(1 << m)]
"""dp[bit][j] := ビット列bitで表される集合に含まれる全ての色を山に含み、j番目の色が一番上に積まれているときの最高得点"""

for i in range(n):
    color = colors[b[i]]
    dp_new = [[-float("inf")] * m for bit in range(1 << m)]
    dp_new[1 << color][color] = p[color]
    for bit in range(1 << m):
        for j in range(m):
            if dp[bit][j] == -float("inf"): continue

            dp_new[bit][j] = max(dp_new[bit][j], dp[bit][j])
            dp_new[bit | (1 << color)][color] = max(dp_new[bit | (1 << color)][color], dp[bit][j] + p[color] + Y * (j == color))

    dp = dp_new

ans = 0
for bit in range(1 << m):
    for j in range(m):
        ans = max(ans, dp[bit][j] + Z * (bit == (1 << m) - 1))

print(ans)