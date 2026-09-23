#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int max_t = 1100001, N, T, A, ans = 0;
    vector<int> open(max_t, 0); // いもす法

    cin >> N >> T;
    for (int i = 0; i < N; i++) {
        cin >> A;
        open[A]++;
        open[A + T]--;
    }

    for (int t = 0; t < max_t - 1; t++) {
        open[t + 1] += open[t];
        if (open[t] > 0) ans++;
    }
    cout << ans << endl;
}