#60点解法
N, Q = map(int, input().split())

board = [0] * N

for _ in range(Q):
    l, r = map(int, input().split())
    for i in range(l-1, r):
        board[i] ^= 1

print(*board, sep="")