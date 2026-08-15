#include <bits/stdc++.h>
using namespace std;

int main() {
    int tx_a, ty_a, tx_b, ty_b, T, V, n, x, y;
    cin >> tx_a >> ty_a >> tx_b >> ty_b >> T >> V >> n;

    string ans = "NO";
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        if (sqrt((x - tx_a) * (x - tx_a) + (y - ty_a) * (y - ty_a)) + sqrt((x - tx_b) * (x - tx_b) + (y - ty_b) * (y - ty_b)) <= V * T) ans = "YES";
    }
    cout << ans << endl;
}