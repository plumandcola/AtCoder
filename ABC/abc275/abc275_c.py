S = [input() for _ in range(9)]

ans = 0
for u in range(9):
    for l in range(9):
        for d in range(9):
            for r in range(9):
                if u == d and l == r: continue
                if S[u][l] != '#' or S[d][r] != '#': continue

                if 0 <= u + r - l < 9 and 0 <= l - d + u < 9 and 0 <= d + r - l < 9 and 0 <= r - d + u < 9 and S[u+r-l][l-d+u] == '#' and S[d+r-l][r-d+u] == '#':
                    ans += 1

print(ans // 4) #同じ正方形を4回数えている