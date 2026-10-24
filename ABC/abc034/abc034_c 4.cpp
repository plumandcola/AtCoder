#include <bits/stdc++.h>
using namespace std;

struct Comb {
    const long long mod;
    vector<long long> fact, fact_inv;

    Comb(long long N, long long mod) : mod(mod), fact(N+1), fact_inv(N+1) {
        fact[0] = 1;
        for (long long i = 1; i <= N; i++) {
            fact[i] = fact[i-1] * i % mod;
        }

        fact_inv[N] = pow(fact[N], mod - 2, mod);
        for (long long i = N-1; i >= 0; i--) {
            fact_inv[i] = fact_inv[i+1] * (i+1) % mod;
        }
    }

    long long pow(long long a, long long b, long long m) {
        // 繰り返し二乗法を用いて、aのb乗をmで割った余りを求める
        long long result = 1;
        while (b) {
            if (b & 1) result = result * a % m;
            a = a * a % m;
            b >>= 1;
        }
        return result;
    }

    long long calc(long long n, long long r) {
        if (r < 0 || r > n) return 0;
        return fact[n] * fact_inv[r] % mod * fact_inv[n-r] % mod;
    }
};

int main() {
    // 101点解法
    long long W, H, mod = 1000000007;
    cin >> W >> H;
    
    Comb comb(W+H-2, mod);

    cout << comb.calc(W+H-2, W-1) << endl;
}