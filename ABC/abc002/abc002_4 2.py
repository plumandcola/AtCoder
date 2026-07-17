def dfs(i: int, members: list[int]) -> int:
    if i == N:
        return len(members)
    
    result = dfs(i+1, members) #議員iを含めない場合

    if all(j in g[i] for j in members):
        members.append(i)
        result = max(result, dfs(i+1, members)) #議員iを含める場合
        members.pop() #元に戻す
    
    return result


N, M = map(int, input().split())

g = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    g[x-1].add(y-1)
    g[y-1].add(x-1)

print(dfs(0, []))