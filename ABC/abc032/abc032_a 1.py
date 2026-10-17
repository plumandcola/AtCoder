def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


a = int(input())
b = int(input())
n = int(input())

lcm = a // gcd(a, b) * b

print((n + lcm - 1) // lcm * lcm)