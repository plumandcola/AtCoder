S = list(input())
T = list("atcoder")

ans = 0
for i in range(7):
    while S[i] != T[i]:
        j = S.index(T[i])
        S[j-1], S[j] = S[j], S[j-1]
        ans += 1

print(ans)