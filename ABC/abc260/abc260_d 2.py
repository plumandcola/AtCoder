from sortedcontainers import SortedList
from collections import deque

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1] * N
S = SortedList()
for i in range(N):
    index = S.bisect_left(deque([[P[i], i]]))

    #場に見えている表向きのカードであって書かれた整数がX以上であるもの、がある場合
    if index < len(S):
        S[index].appendleft([P[i], i])
    
    #ない場合
    else:
        S.add(deque([[P[i], i]]))
    
    #表向きのカードがK枚重ねられた山が場にある場合(今追加されたところだけ確認すれば良い)
    if len(S[index]) == K:
        for j in range(K):
            ans[S[index][j][0] - 1] = i + 1
        #カードを全て食べて、場から消滅させる
        S.pop(index)

print(*ans, sep="\n")