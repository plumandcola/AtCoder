#include <bits/stdc++.h>
using namespace std;

int main() {
    int ans = 0, s, e;
    for (int i = 0; i < 3; i++) {
        cin >> s >> e;
        ans += s * e / 10;
    }

    cout << ans << endl;
}