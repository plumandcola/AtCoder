N, M = map(int, input().split())

B = [0] * N
for i in range(N):
    S = input()
    for j in range(M):
        if S[j] == 'o':
            B[i] |= (1 << j)

mask = (1 << M) - 1

ans = 0
for x in range(N-1):
    for y in range(x+1, N):
        if (B[x] | B[y]) & mask == mask:
            ans += 1

print(ans)