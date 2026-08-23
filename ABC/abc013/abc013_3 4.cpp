#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    long long N, H, A, B, C, D, E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    long long ans = N * C;
    for (long long i = 0; i <= N; i++) { // 普通の食事をとる日数
        for (long long j = 0; j <= N-i; j++) { // 質素な食事をとる日数
            if (H + B * i + D * j - E * (N - i - j) > 0) { // 満腹度が0以下にならないようにできる
                ans = min(ans, A * i + C * j);
            }
        }
    }

    cout << ans << endl;
}
