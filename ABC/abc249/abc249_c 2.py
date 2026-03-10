N, K = map(int, input().split())
S = [0] * N

for i in range(N):
    for c in input():
        S[i] |= 1 << (ord(c) - (ord('a')))

ans = 0
for b in range(1, 1 << N): #b=0はどれも選ばないが、K≥1より不適なので除外
    count = 0
    for i in range(26):
        c = chr(ord('a') + i)
        s = 0
        for j in range(N):
            if (b >> j) & 1 == 1:
                s += (S[j] >> i) & 1
        
        if s == K:
            count += 1
    
    ans = max(ans, count)

print(ans)