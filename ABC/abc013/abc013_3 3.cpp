#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, H, A, B, C, D, E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    long long ans = N * C;
    for (int i = 0; i <= N; i++) { // 普通の食事をとる日数
        for (int j = 0; j <= N-i; j++) { // 質素な食事をとる日数
            long long ans_ij = A * i + C * j; // 食費の合計
            long long s = H + B * i + D * j - E * (N - i - j); // 満腹度
            if (s > 0) ans = min(ans, ans_ij);
        }
    }

    cout << ans << endl;
}