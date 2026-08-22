#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, a, b, t;
    cin >> N >> M;

    vector<vector<int>> d(N, vector<int>(N, 1 << 29));
    for (int i = 0; i < N; i++) d[i][i] = 0;
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> t;
        d[a-1][b-1] = min(d[a-1][b-1], t);
        d[b-1][a-1] = min(d[b-1][a-1], t);
    }

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    int ans = 1 << 30;
    for (int i = 0; i < N; i++) {
        ans = min(ans, *max_element(d[i].begin(), d[i].end()));
    }

    cout << ans << endl;
}