def dfs(n: int, x: int) -> bool:
    #x: 今までのxorの累積
    if n == 0: #全ての質問を探索した
        if x == 0: return True #排他的論理和が0になる選択肢の組み合わせがあった
        else: return False

    result = False
    for t in T[n-1]:
        result |= dfs(n-1, x ^ t)
        #論理和を用いているので、排他的論理和が0になる選択肢の組み合わせが1つでもあればtrueになる
    return result


N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

print("Found" if dfs(N, 0) else "Nothing")