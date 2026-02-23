N = int(input())

ans = 0
m = 0
while m <= N:
    count = min(10 * m + 9, N) - m
    ans = (ans + (1 + count) * count // 2) % 998244353
    m = 10 * m + 9

print(ans)