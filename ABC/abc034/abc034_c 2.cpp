#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int W, H, mod = 1000000007;
    cin >> W >> H;

    vector<vector<int>> ans(H, vector<int>(W, 1));
    for (int i = 1; i < H; i++) {
        for (int j = 1; j < W; j++) {
            ans[i][j] = (ans[i-1][j] + ans[i][j-1]) % mod;
        }
    }

    cout << ans[H-1][W-1] << endl;
}