X, K = map(int, input().split())

pow_10 = [1] * (K+1)
for i in range(K):
    pow_10[i+1] = pow_10[i] * 10

for i in range(K):
    X = (X + 5 * pow_10[i]) // pow_10[i+1] * pow_10[i+1]

print(X)