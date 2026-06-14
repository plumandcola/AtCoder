from sortedcontainers import SortedList

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1] * N
under = [-1] * N #under[i] := i+1の真下に置かれたカード
pile = [-1] * N #pile[i] := i+1が下から何枚目に積まれているか
S = SortedList()
for i in range(N):
    X = P[i]
    index = S.bisect_left(X)

    #場に見えている表向きのカードであって書かれた整数がX以上であるもの、がある場合
    if index < len(S):
        Y = S[index]
        under[X - 1] = Y
        pile[X - 1] = pile[Y - 1] + 1
        S.pop(index)
        S.add(X)
    
    #ない場合
    else:
        pile[X - 1] = 1
        S.add(X)
    
    #表向きのカードがK枚重ねられた山が場にある場合(今追加されたところだけ確認すれば良い)
    if pile[X - 1] == K:
        for j in range(K):
            ans[X-1] = i + 1
            X = under[X-1]
        S.pop(index)

print(*ans, sep="\n")