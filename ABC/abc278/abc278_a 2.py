N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = A[K:] + [0] * min(K, N)

print(*ans)