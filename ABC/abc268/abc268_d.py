def dfs(X: str) -> str:
    if sum(used) == N:
        if 3 <= len(X) <= 16 and X not in T:
            return X
        else:
            return ""
    
    result = ""
    for i in range(N):
        if used[i] == False:
            used[i] = True
            k = 1
            while len(X) + k + len(S[i]) <= 16 and result == "":
                result = dfs(X + '_' * k + S[i])
                k += 1
            used[i] = False
    return result


N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

used = [False] * N
for i in range(N):
    used[i] = True
    ans = dfs(S[i])
    used[i] = False
    if ans != "":
        break

if ans != "":
    print(ans)
else:
    print(-1)
