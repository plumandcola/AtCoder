#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    int ans = 1 << 30;
    for (int x = -100; x <= 100; x++) {
        int s = 0;
        for (int i = 0; i < N; i++) s += (a[i] - x) * (a[i] - x);
        ans = min(ans, s);
    }

    cout << ans << endl;
}