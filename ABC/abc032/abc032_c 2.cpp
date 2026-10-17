#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, K;
    cin >> N >> K;
    vector<int> s(N);
    for (int i = 0; i < N; i++) cin >> s[i];

    if (find(s.begin(), s.end(), 0) != s.end()) {
        cout << N << endl;
        return 0;
    }

    int ans = 0;
    int r = 0;
    long long p = 1;
    for (int l = 0; l < N; l++) {
        while (r < N && p * s[r] <= K) {
            p *= s[r];
            r++;
        }

        if (l != r) {
            ans = max(ans, r - l);
            p /= s[l];
        } else {
            r++;
        }
    }

    cout << ans << endl;
}