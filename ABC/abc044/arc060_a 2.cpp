#include <bits/stdc++.h>
using namespace std;

int main() {
    // 300点解法
    long long N, A;
    cin >> N >> A;
    vector<long long> x(N);
    for (long long i = 0; i < N; i++) cin >> x[i];

    vector<vector<long long>> dp(N+1, vector<long long>(50*N + 1, 0));
    // dp[j][s] := j枚のカードを使って和がsになる場合の数
    dp[0][0] = 1;
    for (long long i = 0; i < N; i++) {
        for (long long j = N-1; j >= 0; j--) {
            for (long long s = 0; s <= 50*N - x[i]; s++) {
                dp[j+1][s + x[i]] += dp[j][s];
            }
        }
    }

    long long ans = 0;
    for (long long i = 1; i <= N; i++) {
        ans += dp[i][i * A];
    }

    cout << ans << endl;
}