#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, X, Y;
    cin >> N >> M >> X >> Y;

    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    vector<int> b(M);
    for (int i = 0; i < M; i++) cin >> b[i];

    int ans = 0, i = 0, j = 0, t = 0;
    // i: aのインデックス, j: bのインデックス, t: 時刻

    while (i < N and j < M) { // 乗れる飛行機がまだ残っている間、ループ
        // 空港Aから乗れる次の飛行機を探す
        while (i < N && a[i] < t) i++;
        // 空港Aから乗れる飛行機が、まだ残っている場合
        if (i < N) {
            t = a[i] + X; // 空港Bに着く時刻

            // 空港Bから乗れる次の飛行機を探す
            while (j < M && b[j] < t) j++;
            if (j < M) { // 空港Bから乗れる飛行機が、まだ残っている場合
                t = b[j] + Y; // 空港Aに着く時刻
                ans++; // 1往復できたので答えに1を足す
            }
        }
    }

    cout << ans << endl;
}