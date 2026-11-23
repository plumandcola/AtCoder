S = input()

ans = 0
tmp = 0
n = len(S)
for b in range(1 << (n-1)):
    for i in range(n):
        tmp += int(S[i])
        if (b >> i) & 1:
            tmp *= 10
        else:
            ans += tmp
            tmp = 0

print(ans)