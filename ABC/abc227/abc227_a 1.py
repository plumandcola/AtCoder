N, K, A = map(int, input().split())

ans = A + K - 1
while ans > N:
    ans -= N

print(ans)