#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, A, B;
    cin >> N >> M;

    vector<vector<int>> d(N, vector<int>(N, 100));
    // d[i][j] := i番目の人からj番目の人までの最短距離、大きめの値で適当に初期化
    for (int i = 0; i < N; i++) d[i][i] = 0;
    for (int i = 0; i < M; i++) {
        cin >> A >> B;
        d[A-1][B-1] = 1;
        d[B-1][A-1] = 1;
    }

    // ワーシャルフロイド法
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    for (int i = 0; i < N; i++) {
        int ans = 0;
        for (int j = 0; j < N; j++) ans += (d[i][j] == 2);
        cout << ans << endl;
    }
}