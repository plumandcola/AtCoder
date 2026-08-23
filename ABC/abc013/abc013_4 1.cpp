#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int N, M, D;
    cin >> N >> M >> D;
    vector<int> A(M);
    for (int i = 0; i < M; i++) cin >> A[i];

    vector<int> amida(N);
    for (int i = 0; i < N; i++) amida[i] = i;
    for (int i = 0; i < D; i++) {
        for (int j = 0; j < M; j++) swap(amida[A[j] - 1], amida[A[j]]);
    }

    vector<int> ans(N);
    for (int i = 0; i < N; i++) ans[amida[i]] = i + 1;

    for (int i = 0; i < N; i++) cout << ans[i] << endl;
}