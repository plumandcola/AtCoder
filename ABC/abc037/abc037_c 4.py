N, K = map(int, input().split())
a = list(map(int, input().split()))

print(sum(a[i] * min(i+1, K, N-K+1, N-i) for i in range(N)))