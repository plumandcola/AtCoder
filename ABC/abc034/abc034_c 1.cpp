#include <bits/stdc++.h>
using namespace std;

int dfs(int W, int H, int mod) {
    if (W == 1 && H == 1) return 1;

    int ans = 0;
    if (W > 1) ans += dfs(W-1, H, mod);
    if (H > 1) ans += dfs(W, H-1, mod);
    return ans % mod;
}

int main() {
    // 50点解法
    int W, H, mod = 1000000007;
    cin >> W >> H;

    if (W <= 10 && H <= 10) cout << dfs(W, H, mod) << endl;
}