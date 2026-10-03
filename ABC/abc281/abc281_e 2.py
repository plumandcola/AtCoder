import heapq

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

q1 = [(A[i], i) for i in range(M)] #のちにq2に入れるもの
heapq.heapify(q1)
q2 = [] #先頭K個(先頭K個からあふれた最大値を取り出すために、符号を反転)
s = 0 #答えとなる和
for _ in range(K):
    #q1から最小値を取り出し、q2へ入れる
    a, i = heapq.heappop(q1)
    heapq.heappush(q2, (-a, i)) #最大値を取り出すために符号を反転
    s += a

ans = [0] * (N-M+1)
ans[0] = s

for i in range(M, N):
    is_contained = False #A[i-M]がsに含まれているかどうか
    if (-A[i-M], i-M) >= q2[0]: #A[i-M]がsに含まれているとき
        is_contained = True
        s -= A[i-M]

    heapq.heappush(q1, (A[i], i))
    #q1から最小値を取り出し、q2へ入れる
    a, j = heapq.heappop(q1)
    while j <= i-M: #i-M+1〜iのいずれかを取り出せるまで取り出し続ける
        a, j = heapq.heappop(q1)
    
    heapq.heappush(q2, (-a, j)) #最大値を取り出すために符号を反転
    s += a
    
    if not is_contained: #A[i-M]がsに含まれていなかったとき
        #q2に1要素加えた分、1要素取り出す
        a, j = heapq.heappop(q2)
        while j <= i-M: #i-M+1〜iのいずれかを取り出せるまで取り出し続ける
            a, j = heapq.heappop(q2)
        s += a #aの符号が反転しているので注意
        heapq.heappush(q1, (-a, j)) #q1に戻す
    
    ans[i-M+1] = s

print(*ans)