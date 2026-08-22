X, K = map(int, input().split())

for i in range(K):
    for _ in range(i): X //= 10
    X = (X//10 + (X%10 >= 5)) * 10
    for _ in range(i): X *= 10

print(X)