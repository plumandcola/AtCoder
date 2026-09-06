#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int N, M, l, r, s;
    cin >> N >> M;

    vector<int> dp(1 << M, 0);
    for (int i = 0; i < N; i++) {
        cin >> l >> r >> s;
        int B = ((1 << (r-l+1)) - 1) << (l-1);
        for (int b = (1 << M) - 1; b >= 0; b--) {
            dp[b | B] = max(dp[b | B], dp[b] + s);
        }
    }

    int ans = 0;
    for (int b = 0; b < (1 << M) - 1; b++) {
        ans = max(ans, dp[b]);
    }

    cout << ans << endl;
}