N, M = map(int, input().split())
S = [input() for _ in range(N)]


to_N = [float("inf")] * N #to_N[i] := 都市iから都市Nまで移動するのに必要なテレポーターの使用回数の最小値
to_N[N-1] = 0
for i in range(N-2, -1, -1):
    for j in range(M):
        if S[i][j] == '1':
            to_N[i] = min(to_N[i], to_N[i+j+1] + 1)


ans = [-1] * (N-2)
from_1 = [float("inf")] * N #from_1[i] := 都市1から都市iまで移動するのに必要なテレポーターの使用回数の最小値
from_1[0] = 0
for i in range(N-1):
    m = float("inf") #都市iを通らずに都市1から都市Nまで移動するのに必要なテレポーターの使用回数の最小値
    for j in range(M):
        if i+j+1 < N:
            m = min(m, from_1[i+j+1] + to_N[i+j+1])
        if S[i][j] == '1':
            from_1[i+j+1] = min(from_1[i+j+1], from_1[i] + 1)

    if m != float("inf") and i > 0:
        ans[i-1] = m

print(*ans)