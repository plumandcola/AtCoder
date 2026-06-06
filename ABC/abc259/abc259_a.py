N, M, X, T, D = map(int, input().split())

print(T if X <= M else T - D * (X - M))