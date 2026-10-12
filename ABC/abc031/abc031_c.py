N = int(input())
a = list(map(int, input().split()))

score_t = [[-float("inf")] * N for _ in range(N)]
"""score_t[i][j] := i番目の要素とj番目の要素が選ばれた時の、高橋君の得点"""
score_a = [[-float("inf")] * N for _ in range(N)]
"""score_a[i][j] := i番目の要素とj番目の要素が選ばれた時の、青木君の得点"""

for i in range(N):
    for j in range(i+1, N): #i>jの場合も、iとjを入れ替えれば得点は同じ
        score_t[i][j] = sum(a[i : j+1 : 2])
        score_t[j][i] = score_t[i][j]
        score_a[i][j] = sum(a[i+1 : j+1 : 2])
        score_a[j][i] = score_a[i][j]

ans = -float("inf")
for i in range(N): #高橋君がi番目の要素を選ぶ時を考える
    j = max(range(N), key = lambda j: score_a[i][j]) #青木君が得点を最も多く得られる要素
    ans = max(ans, score_t[i][j])

print(ans)