from collections import Counter

N, K = map(int, input().split())
S = [Counter(input()) for _ in range(N)]

ans = 0
for b in range(1, 1 << N): #b=0はどれも選ばないが、K≥1より不適なので除外
    count = 0
    for i in range(26):
        c = chr(ord('a') + i)
        s = 0
        for j in range(N):
            if (b >> j) & 1 == 1:
                s += S[j][c]
        
        if s == K:
            count += 1
    
    ans = max(ans, count)

print(ans)