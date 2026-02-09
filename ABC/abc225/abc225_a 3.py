from collections import Counter

def c(n, r):
    r = min(r, n-r)
    ans = 1
    for i in range(n-r+1, n+1):
        ans *= i
    for i in range(2, r+1):
        ans //= i
    return ans


S = input()

ans = 1
n = len(S)
count = Counter(S)
for s in count:
    ans *= c(n, count[s])
    n -= count[s]

print(ans)