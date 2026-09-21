N = int(input())
S = [(A, 0) for A in map(int, input().split())] #S[i][1] := S[i]を最後に更新したタイミング
X = (0, 0) #最後のクエリ1の値とタイミング

Q = int(input())
for q in range(1, Q+1):
    query = list(map(int, input().split()))
    match query[0]:
        case 1:
            x = query[1]
            X = (x, q)
        case 2:
            i = query[1] - 1
            x = query[2]
            if S[i][1] < X[1]: #最後のクエリ1よりも、更新のタイミングが前の場合
                S[i] = (X[0] + x, q)
            else:
                S[i] = (S[i][0] + x, q)
        case 3:
            i = query[1] - 1
            if S[i][1] < X[1]: #最後のクエリ1よりも、更新のタイミングが前の場合
                print(X[0])
            else:
                print(S[i][0])
