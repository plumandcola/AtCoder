N, L = map(int, input().split())

S = [0] * N
for i in range(N):
    for c in input():
        S[i] |= 1 << (ord(c) - ord('a'))

ans = 0
for i in range(1, (1 << N)): #0はどの段も使わないことになるので排除
    b = (1 << 26) - 1
    count = 0 #使える段の数
    for j in range(N):
        if (i >> j) & 1 == 1:
            b &= S[j]
            count += 1
    
    if count % 2 == 1:
        ans = (ans + pow(b.bit_count(), L, 998244353)) % 998244353
    elif count % 2 == 0:
        ans = (ans - pow(b.bit_count(), L, 998244353)) % 998244353

print(ans)