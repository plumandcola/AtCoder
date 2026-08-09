def check(c: list[str], n: int, m: int) -> bool:
    #縦
    for i in range(8):
        if i != n and c[i][m] == 'Q':
            return False
    
    #横
    for j in range(8):
        if j != m and c[n][j] == 'Q':
            return False
    
    #斜め45度
    i = n-1
    j = m-1
    while 0 <= i < 8 and 0 <= j < 8:
        if c[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    i = n+1
    j = m+1
    while 0 <= i < 8 and 0 <= j < 8:
        if c[i][j] == 'Q':
            return False
        i += 1
        j += 1
    
    i = n+1
    j = m-1
    while 0 <= i < 8 and 0 <= j < 8:
        if c[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    
    i = n-1
    j = m+1
    while 0 <= i < 8 and 0 <= j < 8:
        if c[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def dfs(n: int, c: list[str]) -> bool:
    if n == 8:
        for i in range(8):
            print(*c[i], sep="")
        return True
    
    for i in range(8):
        for j in range(8):
            if c[i][j] == '.' and check(c, i, j):
                c[i][j] = 'Q'
                ans = dfs(n+1, c)
                c[i][j] = '.'
                if ans:
                    return True
    
    return False


c = [list(input()) for _ in range(8)]

ans = True
for i in range(8):
    for j in range(8):
        if c[i][j] == 'Q' and check(c, i, j) == False:
            ans = False

if ans == False:
    print("No Answer")
else:
    ans = dfs(3, c)
    if ans == False:
        print("No Answer")
