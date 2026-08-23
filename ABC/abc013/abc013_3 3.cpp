#include <bits/stdc++.h>
using namespace std;

int main() {
    // 40点解法
    long long N, H, A, B, C, D, E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    vector<unordered_map<long long, long long>> dp(N+1);
    dp[0][H] = 0;
    for (long long i = 0; i < N; i++) {
        for (auto [h, m] : dp[i]) {
            if (dp[i+1].find(h+B) == dp[i+1].end()) {
                dp[i+1][h+B] = m + A;
            } else {
                dp[i+1][h+B] = min(dp[i+1][h+B], m + A);
            }

            if (dp[i+1].find(h+D) == dp[i+1].end()) {
                dp[i+1][h+D] = m + C;
            } else {
                dp[i+1][h+D] = min(dp[i+1][h+D], m + C);
            }

            if (h-E > 0) {
                if (dp[i+1].find(h-E) == dp[i+1].end()) {
                    dp[i+1][h-E] = m;
                } else {
                    dp[i+1][h-E] = min(dp[i+1][h-E], m);
                }
            }
        }
    }

    long long ans = 1LL << 62;
    for (auto [h, m] : dp[N]) {
        ans = min(ans, m);
    }
    cout << ans << endl;
}