N, K, X = map(int, input().split())
A = list(map(int, input().split()))

count = sum(A[i] // X for i in range(N)) #限界までX円引きするのに必要なクーポンの枚数
if count >= K: #クーポンK枚ともX円引きできる
    print(sum(A) - K * X)
else:
    R = sorted((A[i] % X for i in range(N)), reverse=True)
    K -= count
    print(sum(R[K:]))