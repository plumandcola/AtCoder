#10点解法
def solve(N: int, M: int):
    for x in range(N+1):
        for y in range(N+1):
            for z in range(N+1):
                if x + y + z == N and 2 * x + 3 * y + 4 * z == M:
                    print(x, y, z)
                    return
    
    print(-1, -1, -1)


N, M = map(int, input().split())

solve(N, M)