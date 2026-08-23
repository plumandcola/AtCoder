#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, M, D;
    cin >> N >> M >> D;
    vector<int> A(M);
    for (int i = 0; i < M; i++) cin >> A[i];

    vector<vector<int>> dp(31, vector<int>(N));
    for (int i = 0; i < N; i++) dp[0][i] = i;

    for (int i = 0; i < M; i++) swap(dp[0][A[i] - 1], dp[0][A[i]]);

    vector<int> amida(N);
    for (int i = 0; i < N; i++) amida[i] = i;
    int i = 0;
    while (D) {
        if (D & 1 == 1) {
            for (int j = 0; j < N; j++) amida[j] = dp[i][amida[j]];
        }
        for (int j = 0; j < N; j++) dp[i+1][j] = dp[i][dp[i][j]];
        D >>= 1;
        i++;
    }

    vector<int> ans(N);
    for (int i = 0; i < N; i++) ans[amida[i]] = i + 1;

    for (int i = 0; i < N; i++) cout << ans[i] << endl;
}