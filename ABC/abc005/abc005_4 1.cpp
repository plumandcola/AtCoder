#include <bits/stdc++.h>
using namespace std;

int calc_sum(const auto& D, int u, int l, int d, int r) {
    int result = 0;
    for (int i = u; i <= d; i++) {
        for (int j = l; j <= r; j++) {
            result += D[i][j];
        }
    }

    return result;
}

int main() {
    // 50点解法
    int N, Q, P;
    cin >> N;
    vector<vector<int>> D(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) cin >> D[i][j];
    }
    
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> P;
        int ans = 0;
        for (int u = 0; u < N; u++) { // 長方形の上
            for (int l = 0; l < N; l++) { // 長方形の左
                for (int d = u; d < N; d++) { // 長方形の下
                    for (int r = l; r < N; r++) { // 長方形の右
                        if ((d - u + 1) * (r - l + 1) <= P) { // 長方形の面積がP以下なら答えを更新
                            ans = max(ans, calc_sum(D, u, l, d, r));
                        }
                    }
                }
            }
        }

        cout << ans << endl;
    }
}