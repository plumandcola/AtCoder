#include <bits/stdc++.h>
using namespace std;

long long power(long long a, long long b) {
    long long result = 1;
    while (b) {
        if (b & 1) result = result * a;
        a = a * a;
        b >>= 1;
    }
    return result;
}

int main() {
    // 10点解法
    int N, H, A, B, C, D, E;
    cin >> N >> H >> A >> B >> C >> D >> E;

    long long ans = N * C;
    for (int b = 0; b < power(3, N); b++) {
        long long ans_i = 0; // 食費の合計
        long long h = H; // 満腹度
        for (int i = 0; i < N; i++) {
            if ((b / power(3, i)) % 3 == 0) {
                ans_i += A;
                h += B;
            } else if ((b / power(3, i)) % 3 == 1) {
                ans_i += C;
                h += D;
            } else if ((b / power(3, i)) % 3 == 2) {
                h -= E;
                if (h <= 0) break;
            }
            if (i == N-1) ans = min(ans, ans_i);
        }
    }
    cout << ans << endl;
}