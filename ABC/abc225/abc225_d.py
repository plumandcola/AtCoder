N, Q = map(int, input().split())

#-1 -> 連結している電車が存在しない
L = [-1] * N
R = [-1] * N
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1] - 1
        y = query[2] - 1
        R[x] = y
        L[y] = x
    elif query[0] == 2:
        x = query[1] - 1
        y = query[2] - 1
        R[x] = -1
        L[y] = -1
    elif query[0] == 3:
        x = query[1] - 1
        ans = [x + 1]

        l = x
        while L[l] != -1:
            l = L[l]
            ans.append(l + 1)
        ans.reverse()
        
        r = x
        while R[r] != -1:
            r = R[r]
            ans.append(r + 1)
        
        print(len(ans), *ans)
