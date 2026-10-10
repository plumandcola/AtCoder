#100点解法
N = int(input()) + 1 #あえて0を個数に含める

ans = 0
for i in range(9):
    ans += N // (10 ** (i+1)) * (10 ** i)
    if N % (10 ** (i+1)) > 2 * (10 ** i):
        ans += (10 ** i)
    elif N % (10 ** (i+1)) > (10 ** i):
        ans += N % (10 ** (i+1)) - (10 ** i)

print(ans)