#include <bits/stdc++.h>
using namespace std;

int main() {
    // 20点解法
    int N, K;
    cin >> N >> K;
    vector<int> s(N);
    for (int i = 0; i < N; i++) cin >> s[i];

    if (find(s.begin(), s.end(), 0) != s.end()) {
        cout << N << endl;
        return 0;
    }

    int ans = 0;
    for (int l = 0; l < N; l++) {
        for (int r = l; r < N; r++) {
            long long p = 1;
            bool ok = true;
            for (int i = l; i <= r; i++) {
                p *= s[i];
                if (p > K) ok = false;
            }

            if (ok) ans = max(ans, r - l + 1);
        }
    }

    cout << ans << endl;
}