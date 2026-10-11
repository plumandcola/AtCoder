m, n, N = map(int, input().split())

ans = N
while N >= m:
    new = N // m * n
    ans += new
    N = new + N % m

print(ans)