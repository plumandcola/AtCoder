#101点解法
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


W, H = map(int, input().split())
mod = 1000000007

comb = Comb(W+H-2, mod)

print(comb.calc(W+H-2, W-1))