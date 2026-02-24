import bisect

is_prime = [True] * 201
is_prime[0] = False #0は素数じゃない
is_prime[1] = False #1は素数じゃない
prime_numbers = []
for n in range(2, 201):
    if is_prime[n]: #nが素数なら
        prime_numbers.append(n)
        for i in range(2*n, 201, n):
            is_prime[i] = False

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    if bisect.bisect_left(prime_numbers, i + C) == bisect.bisect_left(prime_numbers, i + D + 1):
        print("Takahashi")
        break
else:
    print("Aoki")