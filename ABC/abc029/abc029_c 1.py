def dfs(s: str):
    if len(s) == N:
        print(s)
        return
    
    for i in range(3):
        c = chr(ord('a') + i)
        dfs(s + c)


N = int(input())
dfs("")