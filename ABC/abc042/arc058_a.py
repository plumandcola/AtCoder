def check(n: int) -> bool:
    while n:
        if n % 10 in D:
            return False
        n //= 10
    return True


N, K = map(int, input().split())
D = set(map(int, input().split()))

ans = N
while check(ans) == False:
    ans += 1

print(ans)