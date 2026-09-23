#include <bits/stdc++.h>
using namespace std;

int main() {
    // 50点解法
    int max_t = 1100000, N, T, A, ans = 0;
    vector<bool> open(max_t, false);

    cin >> N >> T;
    for (int i = 0; i < N; i++) {
        cin >> A;
        for (int t = A; t < A + T; t++) {
            open[t] = true;
        }
    }

    for (int t = 0; t < max_t; t++) {
        if (open[t] == true) ans++;
    }
    cout << ans << endl;
}