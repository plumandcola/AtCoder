#include <bits/stdc++.h>
using namespace std;

int main() {
    // 101点解法
    long long N, H, A, B, C, D, E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    long long ans = N * C;
    for (long long i = 0; i <= N; i++) { // 普通の食事をとる日数
        long long diff = E * N - (B+E) * i - H; // 満腹度が0以下にならないために、さらに必要な満腹度
        if (diff < 0) {
            ans = min(ans, A * i); // 質素な食事をとる必要がない
            continue;
        }

        long long j = diff / (D + E) + 1; // 満腹度が0以下にならないために、質素な食事をとる必要のある日数
        if (j <= N) {
            ans = min(ans, A * i + C * j);
        }
    }

    cout << ans << endl;
}