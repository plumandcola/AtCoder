#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    // score_t[i][j] := i番目の要素とj番目の要素が選ばれた時の、高橋君の得点
    vector<vector<int>> score_t(N, vector<int>(N, -10000));
    // score_a[i][j] := i番目の要素とj番目の要素が選ばれた時の、青木君の得点
    vector<vector<int>> score_a(N, vector<int>(N, -10000));

    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) { // i>jの場合も、iとjを入れ替えれば得点は同じ
            score_t[i][j] = 0;
            for (int k = i; k <= j; k+= 2) score_t[i][j] += a[k];
            score_t[j][i] = score_t[i][j];

            score_a[i][j] = 0;
            for (int k = i+1; k <= j; k+= 2) score_a[i][j] += a[k];
            score_a[j][i] = score_a[i][j];
        }
    }

    int ans = -10000;
    for (int i = 0; i < N; i++) { // 高橋君がi番目の要素を選ぶ時を考える
        int index_max = 0; // 青木君が得点を最も多く得られる要素
        for (int j = 0; j < N; j++) {
            if (score_a[i][j] > score_a[i][index_max]) index_max = j;
        }
        ans = max(ans, score_t[i][index_max]);
    }

    cout << ans << endl;
}