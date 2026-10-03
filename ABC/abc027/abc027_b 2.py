N = int(input())
a = list(map(int, input().split()))

s = [0] * (N+1) #累積和
for i in range(N):
    s[i+1] = s[i] + a[i]

if s[N] % N != 0:
    print(-1)
else:
    ans = 0
    for i in range(1, N+1):
        if s[i] != i * s[N] // N:
            ans += 1
    
    print(ans)
