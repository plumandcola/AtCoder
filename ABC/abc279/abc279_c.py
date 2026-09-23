H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

S_sorted = sorted("".join(S[i][j] for i in range(H)) for j in range(W))
T_sorted = sorted("".join(T[i][j] for i in range(H)) for j in range(W))

print("Yes" if S_sorted == T_sorted else "No")