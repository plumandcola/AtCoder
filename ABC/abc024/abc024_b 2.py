#100点解法
max_t = 1100001
close = [0] * max_t #close[i] := 時刻iの時点でドアが何秒後に閉まる予定か？

N, T = map(int, input().split())
A = set(int(input()) for _ in range(N))

ans = 0
for t in range(1, max_t):
    if t in A:
        close[t] = T
    else:
        close[t] = max(0, close[t-1] - 1)
    
    ans += (close[t] > 0)

print(ans)