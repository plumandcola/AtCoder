#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int N;
    cin >> N;

    vector<int> w(N), h(N);
    for (int i = 0; i < N; i++) cin >> w[i] >> h[i];

    vector<int> memo(N, -1);

    auto dp = [&](auto&& self, int i) -> int {
        if (memo[i] != -1) return memo[i];

        int result = 1;

        for (int j = 0; j < N; j++) {
            if (h[j] < h[i] && w[j] < w[i]) {
                result = max(result, self(self, j) + 1);
            }
        }

        return memo[i] = result;
    };

    int ans = 0;
    for (int i = 0; i < N; i++) {
        ans = max(ans, dp(dp, i));
    }
    cout << ans << endl;
}