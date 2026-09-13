N, L = map(int, input().split())

ans = list(range(1, N+1))
for _ in range(L):
    x = input()
    for i in range(N-1):
        if x[2*i + 1] == '-':
            ans[i], ans[i+1] = ans[i+1], ans[i]

y = input()
for i in range(N):
    if y[2*i] == 'o':
        print(ans[i])
