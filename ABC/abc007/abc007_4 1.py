#30点解法
def is_banned(n: int) -> bool:
    while n:
        if n % 10 == 4 or n % 10 == 9:
            return True
        n //= 10
    return False

A, B = map(int, input().split())

print(sum(is_banned(i) for i in range(A, B+1)))