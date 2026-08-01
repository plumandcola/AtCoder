#30点解法
def solve(N: int, M: int):
    for x in range(N+1):
        for y in range(N-x+1):
            z = N - x - y
            if 2 * x + 3 * y + 4 * z == M: #z >= 0であることは、y < N-x+1から保証されている
                print(x, y, z)
                return
    
    print(-1, -1, -1)


N, M = map(int, input().split())

solve(N, M)