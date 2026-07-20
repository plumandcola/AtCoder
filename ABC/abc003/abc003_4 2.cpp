#include <bits/stdc++.h>
using namespace std;

long long calc_c(const auto& c, long long n, long long r) { // 二項係数nCrを返す
    if (r < 0 || r > n) return 0;
    else return c[n][r];
}

int main() {
    // 101点解法
    long long R, C, X, Y, D, L, mod = 1000000007;
    cin >> R >> C >> X >> Y >> D >> L;
    
    vector<vector<long long>> c(X*Y + 1, vector<long long>(0)); // パスカルの三角形を用いて二項係数を求める
    for (long long i = 0; i <= X*Y; i++) {
        c[i].push_back(1);
        for (long long j = 1; j <= i-1; j++) c[i].push_back((c[i-1][j-1] + c[i-1][j]) % mod);
        c[i].push_back(1);
    }
    
    vector<vector<long long>> dp(X + 1, vector<long long>(Y + 1, 0));
    // dp[x][y] := ちょうどx行y列の区画に、D個のデスクトップとL個のサーバーラックを配置するパターン数
    for (long long x = 1; x <= X; x++) {
        for (long long y = 1; y <= Y; y++) {
            dp[x][y] = calc_c(c, x*y, D) * calc_c(c, x*y - D, L) % mod;
            for (long long i = 1; i <= x; i++) {
                for (long long j = 1; j <= y; j++) {
                    if (i != x || j != y) {
                        dp[x][y] -= dp[i][j] * (x-i+1) * (y-j+1);
                        dp[x][y] = (dp[x][y] % mod + mod) % mod; // 引き算をして負になっても、余りが正になるようにする
                    }
                }
            }
        }
    }

    cout << dp[X][Y] * (R-X+1) * (C-Y+1) % mod << endl;
}