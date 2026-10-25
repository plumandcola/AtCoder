#include <bits/stdc++.h>
using namespace std;

int main() {
    // 50点解法
    long long N, M, T, a, b, c;
    cin >> N >> M >> T;
    vector<long long> A(N);
    for (long long i = 0; i < N; i++) cin >> A[i];
    const long long INF = 1LL << 61;

    vector<vector<long long>> d(N, vector<long long>(N, INF));
    for (long long i = 0; i < N; i++) d[i][i] = 0;
    for (long long i = 0; i < M; i++) {
        cin >> a >> b >> c;
        d[a-1][b-1] = c;
    }

    // ワーシャルフロイド法
    for (long long k = 0; k < N; k++) {
        for (long long i = 0; i < N; i++) {
            for (long long j = 0; j < N; j++) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }

    long long ans = 0;
    for (long long i = 0; i < N; i++) {
        if (d[0][i] != INF && d[i][0] != INF) {
            ans = max(ans, A[i] * (T - d[0][i] - d[i][0]));
        }
    }

    cout << ans << endl;
}