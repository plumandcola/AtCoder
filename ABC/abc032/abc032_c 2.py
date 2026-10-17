#100点解法
N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
else:
    ans = 0
    r = 0
    p = 1
    for l in range(N):
        while r < N and p * s[r] <= K:
            p *= s[r]
            r += 1
        
        if l != r:
            ans = max(ans, r - l)
            p //= s[l]
        else:
            r += 1
    
    print(ans)