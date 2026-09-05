#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, A, B;
    cin >> N >> M;

    vector<vector<int>> g(N, vector<int>(N, 0));
    for (int i = 0; i < M; i++) {
        cin >> A >> B;
        g[A-1][B-1] = 1;
        g[B-1][A-1] = 1;
    }

    for (int i = 0; i < N; i++) { // i番目のユーザについて調べる
        vector<bool> ans(N, false);
        for (int j = 0; j < N; j++) { // j番目のユーザが「友達の友達」かどうかを調べる
            for (int k = 0; k < N; k++) { // i番目のユーザとk番目のユーザが友達、かつk番目のユーザとj番目のユーザが友達かどうかを調べる
                if (g[i][k] == 1 && g[k][j] == 1 && j != i and g[i][j] == 0) ans[j] = true;
                // 自分自身や友達でないことも確認
            }
        }

        int s = 0;
        for (int j = 0; j < N; j++) s += ans[j];
        cout << s << endl;
    }
}