#include <bits/stdc++.h>
using namespace std;

int main() {
    // 20点解法
    int N, ans = 0, dist;
    cin >> N;

    for (int i = 1; i <= N-1; i++) {
        for (int j = i+1; j <= N; j++) {
            cout << "? " << i << " " << j << endl;
            cin >> dist;
            ans = max(ans, dist);
        }
    }

    cout << "! " << ans << endl;
}