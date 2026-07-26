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
    
    cin >> Q;
    for (int q = 0; q < Q; q++) {
        cin >> P;
        int ans = 0;
        for (int H = 1; H <= N && H <= P; H++) { // 長方形の縦の長さ
            int W = min(N, P / H); // 長方形の横の長さ(できるだけ長い方がいい)
            for (int i = 0; i <= N-H; i++) { // 長方形の上
                for (int j = 0; j <= N-W; j++) { // 長方形の左
                    ans = max(ans, s[i+H][j+W] - s[i+H][j] - s[i][j+W] + s[i][j]);
                }
            }
        }

        cout << ans << endl;
    }
}