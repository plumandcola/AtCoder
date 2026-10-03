from sortedcontainers import SortedList

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

S = SortedList()
for i in range(M):
    S.add((A[i], i))

s = sum(S[i][0] for i in range(K)) #答えとなる和

ans = [0] * (N-M+1)
ans[0] = s

for i in range(M, N):
    j = S.bisect_left((A[i-M], i-M))
    if j < K:
        s -= A[i-M]
        if len(S) > K:
            s += S[K][0]
    S.pop(j)

    S.add((A[i], i))
    j = S.bisect_left((A[i], i))
    if j < K:
        s += A[i]
        if len(S) > K:
            s -= S[K][0]
    
    ans[i-M+1] = s

print(*ans)