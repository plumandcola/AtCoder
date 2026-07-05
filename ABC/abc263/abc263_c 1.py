def dfs(ans: list[int], N: int, M: int, last: int):
    if len(ans) == N:
        print(*ans)
        return
    
    for i in range(last + 1, M + 1):
        ans.append(i)
        dfs(ans, N, M, i)
        ans.pop()


N, M = map(int, input().split())
dfs([], N, M, 0)