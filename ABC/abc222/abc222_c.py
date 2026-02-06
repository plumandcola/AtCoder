def is_winner(A: list[str], i: int, n: int, m: int) -> bool:
    """iラウンド目で人nが人mに、勝つか(True)、引き分けか負けか(False)"""
    if A[n][i] == 'G' and A[m][i] == 'C':
        return True
    elif A[n][i] == 'C' and A[m][i] == 'P':
        return True
    elif A[n][i] == 'P' and A[m][i] == 'G':
        return True
    else:
        return False


N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]

standings = [[] for _ in range(M+1)]
standings[0] = [(0, i) for i in range(2*N)]
for i in range(M):
    for k in range(N):
        count_n, n = standings[i][2*k] #片方の人の勝数と番号
        count_m, m = standings[i][2*k + 1] #もう片方の人の勝数と番号
    
        if is_winner(A, i, n, m):
            standings[i+1].append((count_n - 1, n)) #勝数が多い方が昇順ソートで前に来るように、マイナスにする
        else:
            standings[i+1].append((count_n, n))
    
        if is_winner(A, i, m, n):
            standings[i+1].append((count_m - 1, m))
        else:
            standings[i+1].append((count_m, m))
    
    standings[i+1].sort()

for k in range(2*N):
    print(standings[M][k][1] + 1) #0-indexedになっているので1足す