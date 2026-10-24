#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int W, H, mod = 1000000007;
    cin >> W >> H;

    vector<vector<long long>> c(W+H-1, vector<long long>(0)); // パスカルの三角形を用いて二項係数を求める
    for (int i = 0; i < W+H-1; i++) {
        c[i].push_back(1LL);
        for (int j = 1; j <= i-1; j++) c[i].push_back((c[i-1][j-1] + c[i-1][j]) % mod);
        c[i].push_back(1LL);
    }

    cout << c[W+H-2][W-1] << endl;
}