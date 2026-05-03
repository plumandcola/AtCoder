N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(K):
    a[i::K] = sorted(a[i::K])

print("Yes" if a == sorted(a) else "No")