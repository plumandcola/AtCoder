X = int(input())

ans = 0
while X:
    ans += X % 10
    X //= 10

print(ans)