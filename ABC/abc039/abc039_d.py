H, W = map(int, input().split())
S = [input() for _ in range(H)]

image = [['#'] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            for h in range(max(0, i-1), min(H, i+2)):
                for w in range(max(0, j-1), min(W, j+2)):
                    image[h][w] = '.'

ans = "possible"
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            possible = False
            for h in range(max(0, i-1), min(H, i+2)):
                for w in range(max(0, j-1), min(W, j+2)):
                    if image[h][w] == '#':
                        possible = True
            if possible == False:
                ans = "impossible"

print(ans)
if ans == "possible":
    for i in range(H):
        print(*image[i], sep="")
