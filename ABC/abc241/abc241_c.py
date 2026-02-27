N = int(input())
S = [input() for _ in range(N)]

ans = False

#縦
for i in range(N-5):
    for j in range(N):
        if sum(S[i+k][j] == '.' for k in range(6)) <= 2:
            ans = True

#横
for i in range(N):
    for j in range(N-5):
        if sum(S[i][j+k] == '.' for k in range(6)) <= 2:
            ans = True

#斜め
for i in range(N-5):
    for j in range(N-5):
        if sum(S[i+k][j+k] == '.' for k in range(6)) <= 2:
            ans = True
        if sum(S[i+k][j+5-k] == '.' for k in range(6)) <= 2:
            ans = True

print("Yes" if ans else "No")