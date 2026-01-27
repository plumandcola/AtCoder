S, T = map(int, input().split())

ans = 0
for a in range(S+1):
    for b in range(S-a+1):
        if a*b == 0:
            ans += S-a-b+1
        else:
            ans += min(S-a-b, T//a//b) + 1

print(ans)