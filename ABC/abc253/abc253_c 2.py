from sortedcontainers import SortedList

S = SortedList()

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 3:
        print(S[-1][0] - S[0][0])
        continue
    
    x = query[1]
    i = S.bisect_left([x, 0])
    if query[0] == 1:
        if i < len(S) and S[i][0] == x: #Sにxが既に存在する場合
            S[i][1] += 1
        else: #Sにxが存在しない場合
            S.add([x, 1])
    elif query[0] == 2:
        c = query[2]
        if i >= len(S) or S[i][0] != x: #Sにxが存在しない場合
            continue
        elif S[i][1] > c: #Sにxが、c個より多く存在する場合
            S[i][1] -= c
        else:
            S.pop(i)
