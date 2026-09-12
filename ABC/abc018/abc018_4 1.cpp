#include <bits/stdc++.h>
using namespace std;

int popcount(int n) {
    int result = 0;
    while (n) {
        result += n & 1;
        n >>= 1;
    }
    return result;
}

int main() {
    // 30点解法
    int N, M, P, Q, R;
    cin >> N >> M >> P >> Q >> R;

    vector<int> x(R), y(R), z(R);
    for (int i = 0; i < R; i++) {
        cin >> x[i] >> y[i] >> z[i];
        x[i]--;
        y[i]--;
    }

    int ans = 0;
    for (int b_g = 0; b_g < (1 << N); b_g++) {
        if (popcount(b_g) != P) continue;

        for (int b_b = 0; b_b < (1 << M); b_b++) {
            if (popcount(b_b) != Q) continue;

            int s = 0;
            for (int i = 0; i < R; i++) {
                if (((b_g >> x[i]) & 1) && ((b_b >> y[i]) & 1)) {
                    s += z[i];
                }
            }

            ans = max(ans, s);
        }
    }

    cout << ans << endl;
}