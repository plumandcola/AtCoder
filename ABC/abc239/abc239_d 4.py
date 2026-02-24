is_prime = [True] * 201
is_prime[0] = False #0は素数じゃない
is_prime[1] = False #1は素数じゃない
s = [0] * 201
for n in range(2, 201):
    if is_prime[n]: #nが素数なら
        for i in range(2*n, 201, n):
            is_prime[i] = False
    
    s[n] = s[n-1] + is_prime[n]

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    if s[i + D] - s[i + C - 1] == 0:
        print("Takahashi")
        break
else:
    print("Aoki")