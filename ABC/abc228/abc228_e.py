N, K, M = map(int, input().split())

if M % 998244353 == 0:
    print(0)
else:
    print(pow(M, pow(K, N, 998244352), 998244353))