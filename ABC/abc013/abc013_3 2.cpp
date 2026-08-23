#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    long long N, H, A, B, C, D, E, INF = 1LL << 62;
    cin >> N >> H >> A >> B >> C >> D >> E;

    vector<vector<long long>> dp(N+1, vector<long long>(H + N*B + 1, INF));
    dp[0][H] = 0;
    for (long long i = 0; i < N; i++) { // i日目
        for (long long h = 1; h <= H + N*B; h++) { // 満腹度h
            if (dp[i][h] == INF) continue; // i日目に満腹度がhであることは不可能

            dp[i+1][h+B] = min(dp[i+1][h+B], dp[i][h] + A);
            dp[i+1][h+D] = min(dp[i+1][h+D], dp[i][h] + C);
            if (h > E) { // h-E > 0なら
                dp[i+1][h-E] = min(dp[i+1][h-E], dp[i][h]);
            }
        }
    }

    long long ans = INF;
    for (long long h = 1; h <= H + N*B; h++) {
        ans = min(ans, dp[N][h]);
    }
    cout << ans << endl;
}
