#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, ans = 0;
    long long X;
    cin >> n >> X;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < n; i++) {
        if ((X >> i) & 1 == 1) ans += a[i];
    }

    cout << ans << endl;
}