S = [input() for _ in range(3)]
T = map(int, input())

ans = ""
for t in T:
    ans += S[t-1]

print(ans)