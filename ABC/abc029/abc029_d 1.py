#20点解法
def count(n: int) -> int:
    result = 0
    while n:
        result += (n % 10 == 1)
        n //= 10
    return result

N = int(input())

print(sum(count(i) for i in range(1, N+1)))