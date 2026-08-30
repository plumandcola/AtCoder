from collections import defaultdict

class Comb:
    def __init__(self, N: int, mod: int):
        self.mod = mod

        self.fact = [1] * (N+1)
        for i in range(1, N+1):
            self.fact[i] = self.fact[i-1] * i % self.mod

        self.fact_inv = [1] * (N+1)
        self.fact_inv[N] = pow(self.fact[N], self.mod - 2, self.mod)
        for i in range(N-1, -1, -1):
            self.fact_inv[i] = self.fact_inv[i+1] * (i+1) % self.mod
    
    def calc(self, n: int, r: int) -> int:
        if r < 0 or r > n:
            return 0
        
        return self.fact[n] * self.fact_inv[r] % self.mod * self.fact_inv[n-r] % self.mod


N, M = map(int, input().split())
mod = 1000000007

#素因数分解
n = abs(N)
prime_factors = defaultdict(int)
for i in range(2, int(n**0.5) + 1):
    while n % i == 0:
        prime_factors[i] += 1
        n //= i
if n != 1:
    prime_factors[n] += 1

comb = Comb(M+29, mod)

ans = 1
for n in prime_factors.values():
    ans = ans * comb.calc(n+M-1, n) % mod

print(ans * pow(2, M-1, mod) % mod)