#include <bits/stdc++.h>
using namespace std;

int main() {
    // 300点解法
    long long N, A;
    cin >> N >> A;
    vector<long long> x(N);
    for (long long i = 0; i < N; i++) cin >> x[i];

    vector<unordered_map<long long, long long>> dp(N+1);
    // dp[i][s] := i番目までのカードを使って、x - Aの和がsになる場合の数
    dp[0][0] = 1;
    for (long long i = 0; i < N; i++) {
        for (auto [s, count] : dp[i]) {
            dp[i+1][s] += count;
            dp[i+1][s + x[i] - A] += count;
        }
    }

    cout << dp[N][0] - 1 << endl; // 0枚の場合を引く
}