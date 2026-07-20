#include <bits/stdc++.h>
using namespace std;

long long pow(long long a, long long b, long long mod) {
    // 繰り返し二乗法を用いて、aのb乗をmodで割った余りを求める
    long long result = 1;
    while (b) {
        if (b & 1) result = result * a % mod;
        a = a * a % mod;
        b >>= 1;
    }
    return result;
}

long long c(long long n, long long r, long long mod) {
    r = min(r, n-r);
    if (r < 0) return 0;

    long long ans = 1;
    for (long long i = n-r+1; i <= n; i++) ans = ans * i % mod;
    for (long long i = 2; i <= r; i++) ans = ans * pow(i, mod - 2, mod) % mod;
    return ans;
}

int main() {
    // 100点解法
    long long R, C, X, Y, D, L, mod = 1000000007;
    cin >> R >> C >> X >> Y >> D >> L;
    cout << c(X*Y, D, mod) * (R-X+1) * (C-Y+1) % mod << endl;
}