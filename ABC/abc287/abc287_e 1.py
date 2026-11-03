N = int(input())
S = sorted((input(), i) for i in range(N))

LCP = [0] * (N-1)
for i in range(N-1):
    x = S[i][0]
    y = S[i+1][0]
    while LCP[i] < len(x) and LCP[i] < len(y) and x[LCP[i]] == y[LCP[i]]:
        LCP[i] += 1

ans = [0] * N
ans[S[0][1]] = LCP[0]
for j in range(1, N-1):
    ans[S[j][1]] = max(LCP[j-1], LCP[j])
ans[S[N-1][1]] = LCP[N-2]

print(*ans, sep="\n")