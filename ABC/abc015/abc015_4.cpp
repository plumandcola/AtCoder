#include <bits/stdc++.h>
using namespace std;

int main() {
    int W, N, K, A, B;
    cin >> W >> N >> K;

    vector<vector<int>> dp(K+1, vector<int>(W+1, 0));
    // dp[i][j] := i枚のスクリーンショットを貼りつけてjの幅を使った時の、重要度の合計の最大値
    for (int n = 0; n < N; n++) {
        cin >> A >> B;
        for (int i = K-1; i >= 0; i--) {
            for (int j = W-A; j >= 0; j--) {
                dp[i+1][j+A] = max(dp[i+1][j+A], dp[i][j] + B);
            }
        }
    }

    int ans = 0;
    for (int i = 0; i <= K; i++) {
        for (int j = 0; j <= W; j++) {
            ans = max(ans, dp[i][j]);
        }
    }
    cout << ans << endl;
}