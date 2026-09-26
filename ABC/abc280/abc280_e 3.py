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


N, P = map(int, input().split())
mod = 998244353

comb = Comb(N, mod)
inv_100 = pow(100, mod - 2, mod)

critical = [1] * (N+1)
for i in range(N):
    critical[i+1] = critical[i] * P % mod * inv_100 % mod

normal = [1] * (N+1)
for i in range(N):
    normal[i+1] = normal[i] * (100 - P) % mod * inv_100 % mod

ans = 0
for k in range(N//2 + 1):
    ans = (ans + comb.calc(N-k, k) * critical[k] % mod * normal[N - 2*k] % mod * (N-k) % mod) % mod

for k in range((N-1)//2 + 1):
    ans = (ans + comb.calc(N-k-1, k) * critical[k+1] % mod * normal[N - 2*k - 1] * (N-k) % mod) % mod

print(ans)