X, K = map(int, input().split())

pow_10_K = pow(10, K)

print((X + pow_10_K // 9 * 5) // pow_10_K * pow_10_K)