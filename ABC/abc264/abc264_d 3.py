n = 7
S = input()
T = "atcoder"

ans = 0
atc = {c: i for i, c in enumerate("atcoder")}
a = [atc[S[i]] for i in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] > a[j]:
            ans += 1

print(ans)