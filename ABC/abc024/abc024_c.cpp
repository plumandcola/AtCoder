#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, D, K;
    cin >> N >> D >> K;
    vector<int> L(D), R(D), S(K), T(K);
    for (int i = 0; i < D; i++) cin >> L[i] >> R[i];
    for (int i = 0; i < K; i++) cin >> S[i] >> T[i];

    for (int i = 0; i < K; i++) { // i番目の民族について
        int l = S[i], r = S[i]; // 現時点で行き来できる街の左端・右端
        for (int d = 0; d < D; d++) {
            if (l <= R[d] && r >= L[d]) { // 行き来できる街の範囲を伸ばせる
                l = min(l, L[d]);
                r = max(r, R[d]);
                if (l <= T[i] && T[i] <= r) { // 街T[i]に到着できる
                    cout << d + 1 << endl;
                    break;
                }
            }
        }
    }
}