#100点解法
N, Q = map(int, input().split())

board = [0] * (N+1) #いもす法

for _ in range(Q):
    l, r = map(int, input().split())
    board[l-1] += 1
    board[r] -= 1

for i in range(N):
    print(board[i] % 2, end="")
    board[i+1] += board[i]
print()