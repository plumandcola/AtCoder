import sys
sys.setrecursionlimit(10000000)


N = int(input())
S = [input() for _ in range(N)]

ans = [0] * N

def dfs(i: int, indices: list[int]):
    groups = [[] for _ in range(26)]
    for index in indices:
        ans[index] = i
        if i < len(S[index]):
            groups[ord(S[index][i]) - ord('a')].append(index)

    for group in groups:
        if len(group) >= 2:
            dfs(i+1, group)

dfs(0, list(range(N)))

print(*ans, sep="\n")