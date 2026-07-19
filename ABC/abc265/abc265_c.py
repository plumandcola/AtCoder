H, W = map(int, input().split())
G = [input() for _ in range(H)]

i = 0
j = 0
visited = [[False] * W for _ in range(H)]
while True:
    if visited[i][j] == True:
        print(-1)
        break

    visited[i][j] = True
    if G[i][j] == 'U':
        if i != 0:
            i -= 1
            continue
    elif G[i][j] == 'D':
        if i != H-1:
            i += 1
            continue
    elif G[i][j] == 'L':
        if j != 0:
            j -= 1
            continue
    elif G[i][j] == 'R':
        if j != W-1:
            j += 1
            continue
    
    #移動することができない場合
    print(i+1, j+1)
    break
