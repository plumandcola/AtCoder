n, X = map(int, input().split())
a = list(map(int, input().split()))

print(sum(a[i] for i in range(n) if (X >> i) & 1 == 1))