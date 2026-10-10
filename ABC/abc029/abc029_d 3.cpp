#include <bits/stdc++.h>
using namespace std;
using vll = vector<long long>;

int main() {
    // 100点解法
    string N;
    cin >> N;
    int n = N.size();
    vector<vector<vll>> dp(n+1, vector<vll>(2, vll(n+1, 0)));
    // dp[i][b][j], j: 1が何個含まれているか
    dp[0][0][0] = 1;
    for (int i = 0; i < n; i++) {
        for (int b = 0; b < 2; b++) {
            int limit = b == 1 ? 9 : N[i] - '0';
            for (int j = 0; j < n; j++) {
                for (int d = 0; d <= limit; d++) {
                    int B = b | (d < (N[i] - '0'));
                    int J = j + (d == 1);
                    dp[i+1][B][J] += dp[i][b][j];
                }
            }
        }
    }

    int ans = 0;
    for (int j = 0; j <= n; j++) {
        ans += (dp[n][0][j] + dp[n][1][j]) * j;
    }

    cout << ans << endl;
}