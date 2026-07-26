#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q, P;
    cin >> N;
    vector<vector<int>> D(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) cin >> D[i][j];
    }
    
    vector<vector<int>> s(N+1, vector<int>(N+1)); // 二次元累積和
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + D[i][j];
        }
    }

    vector<int> ans(N * N + 1); // ans[i] := 面積がi以下の長方形で焼けるたこ焼きの美味しさの合計の最大値

    for (int u = 0; u < N; u++) { // 長方形の上
        for (int l = 0; l < N; l++) { // 長方形の左
            for (int d = u; d < N; d++) { // 長方形の下
                for (int r = l; r < N; r++) { // 長方形の右
                    int area = (d - u + 1) * (r - l + 1); // 長方形の面積
                    ans[area] = max(ans[area], s[d+1][r+1] - s[d+1][l] - s[u][r+1] + s[u][l]);
                }
            }
        }
    }

    for (int i = 0; i < N * N; i++) ans[i+1] = max(ans[i+1], ans[i]);
    
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        cin >> P;
        cout << ans[P] << endl;
    }
}