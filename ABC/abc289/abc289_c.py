N, M = map(int, input().split())

C = [0] * M
S = [0] * M #集合S_iを、長さNのビット列で表す
for i in range(M):
    C[i] = int(input())
    for a in map(int, input().split()):
        S[i] |= 1 << (a-1)

ans = 0
mask = (1 << N) - 1 #1〜Nのすべての整数を含む集合を表すビット列
for b in range(1, 1 << M): #S_iの選び方をbit全探索
    B = 0 #選んだS_iのビット列のor
    for i in range(M):
        if (b >> i) & 1:
            B |= S[i]

    if B == mask: #1〜Nのすべての整数が、選んだS_iのいずれかに含まれる
        ans += 1

print(ans)