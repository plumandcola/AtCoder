N = int(input())

g = [[] for _ in range(N)]
for i in range(1, N):
    B = int(input())
    g[B-1].append(i)

salaries = [-1] * N #salaries[i] := 社員番号がiの社員の給料

def dfs(v: int):
    #直属の部下がいない場合
    if len(g[v]) == 0:
        salaries[v] = 1

    #直属の部下がいる場合
    else:
        M = 0 #max
        m = float("inf") #min
        for u in g[v]:
            dfs(u)

            M = max(M, salaries[u])
            m = min(m, salaries[u])
        
        salaries[v] = M + m + 1

dfs(0)
print(salaries[0])