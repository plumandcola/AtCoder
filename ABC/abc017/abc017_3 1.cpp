#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int N, M, ans = 0;
    cin >> N >> M;

    vector<int> l(N), r(N), s(N);
    for (int i = 0; i < N; i++) cin >> l[i] >> r[i] >> s[i];

    for (int b = 0; b < (1 << N); b++) {
        int S = 0;
        vector<bool> jewels(M, false);
        for (int i = 0; i < N; i++) {
            if ((b >> i) & 1) {
                S += s[i];
                for (int j = l[i] - 1; j < r[i]; j++) jewels[j] = true;
            }
        }

        for (int j = 0; j < M; j++) {
            if (jewels[j] == false) { // 獲得していない宝石がある
                ans = max(ans, S);
                break;
            }
        }
    }

    cout << ans << endl;
}