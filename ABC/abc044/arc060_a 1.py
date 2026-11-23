#200点解法
N, A = map(int, input().split())
x = list(map(int, input().split()))

ans = 0
for b in range(1, 1 << N): #bit全探索
    s = 0
    n = 0
    for i in range(N):
        if (b >> i) & 1:
            s += x[i]
            n += 1
    
    if s == n * A:
        ans += 1

print(ans)