N, M = map(int, input().split())

g = [[False] * N for _ in range(N)]
"""g[i][j] := 議員iと議員j(i<j)が知り合いかどうか"""
for _ in range(M):
    x, y = map(int, input().split())
    g[x-1][y-1] = True

ans = 0
for b in range(1 << N): #bit全探索
    ok = True
    for i in range(N-1):
        if (b >> i) & 1 == 0:
            continue
        for j in range(i+1, N):
            if (b >> j) & 1 == 0:
                continue
            
            if g[i][j] == False: #議員iと議員jがともに派閥に属するが、知り合いでない
                ok = False
    
    if ok == True:
        ans = max(ans, b.bit_count())

print(ans)