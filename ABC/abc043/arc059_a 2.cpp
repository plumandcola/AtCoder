#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, s = 0, ss = 0;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        s += a[i];
        ss += a[i] * a[i];
    }

    int ans = 1 << 30;
    for (int x = -100; x <= 100; x++) {
        ans = min(ans, ss - 2 * s * x + N * x * x);
    }

    cout << ans << endl;
}