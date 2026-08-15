#99点解法
import sys
sys.setrecursionlimit(1000000)


def dfs(v):
    for u in g[v]:
        if trackable[u] == False:
            trackable[u] = True
            dfs(u)


N, G, E = map(int, input().split())
p = list(map(int, input().split()))

friends = [tuple(map(int, input().split())) for _ in range(E)]

ans = float("inf")
for i in range(1 << E): #bit全探索
    ans_i = 0
    trackable = [False] * N #高橋君が辿ることが可能かどうか
    g = [[] for _ in range(N)]
    for j in range(E):
        a, b = friends[j]
        if (i >> j) & 1 == 1: #二人の友人関係を解消する
            ans_i += 1
        else: #二人の友人関係はそのまま
            g[a].append(b)
            g[b].append(a)
    
    dfs(0) #dfs(再帰)
    
    for j in range(G):
        if trackable[p[j]] == True: #パスワードを変え、ログイン出来なくする
            ans_i += 1
    ans = min(ans, ans_i)

print(ans)