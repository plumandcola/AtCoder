#include <bits/stdc++.h>
using namespace std;

int main() {
    // 200点解法
    int N, A;
    cin >> N >> A;
    vector<int> x(N);
    for (int i = 0; i < N; i++) cin >> x[i];

    int ans = 0;
    for (int b = 1; b < (1 << N); b++) { // bit全探索
        int s = 0;
        int n = 0;
        for (int i = 0; i < N; i++) {
            if ((b >> i) & 1) {
                s += x[i];
                n++;
            }
        }

        if (s == n * A) ans++;
    }

    cout << ans << endl;
}