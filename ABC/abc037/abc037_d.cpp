#include <bits/stdc++.h>
using namespace std;

long long f(int i, int j, int& H, int& W, long long& mod, auto& dp, auto& a) {
    if (dp[i][j] != -1) return dp[i][j];
    else {
        long long ans = 1;
        if (i-1 >= 0 && a[i-1][j] < a[i][j]) ans += f(i-1, j, H, W, mod, dp, a);
        if (i+1 < H && a[i+1][j] < a[i][j]) ans += f(i+1, j, H, W, mod, dp, a);
        if (j-1 >= 0 && a[i][j-1] < a[i][j]) ans += f(i, j-1, H, W, mod, dp, a);
        if (j+1 < W && a[i][j+1] < a[i][j]) ans += f(i, j+1, H, W, mod, dp, a);

        ans %= mod;
        dp[i][j] = ans;
        return ans;
    }
}

int main() {
    int H, W;
    cin >> H >> W;
    vector<vector<int>> a(H, vector<int>(W));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            cin >> a[i][j];
        }
    }
    long long mod = 1000000007;

    long long ans = 0;
    vector<vector<long long>> dp(H, vector<long long>(W, -1));

    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            ans += f(i, j, H, W, mod, dp, a);
        }
    }
    cout << ans % mod << endl;
}