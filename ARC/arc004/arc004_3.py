X, Y = map(int, input().split('/'))

impossible = True
for N in range(2*X // Y, 2*X // Y + 2):
    M = N * (N+1) // 2 - N * X // Y
    if 0 < M <= N and (N * (N+1) // 2 - M) * Y == X * N:
        print(N, M)
        impossible = False

if impossible:
    print("Impossible")
