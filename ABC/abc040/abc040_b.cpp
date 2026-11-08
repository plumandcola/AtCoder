#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int ans = 1 << 30;
    for (int i = 1; i * i <= n; i++) {
        int j = n / i;
        ans = min(ans, abs(i - j) + (n - i * j));
    }

    cout << ans << endl;
}