#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N), s(N+1, 0);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        s[i+1] = s[i] + a[i];
    }

    if (s[N] % N != 0) {
        cout << -1 << endl;
        return 0;
    }

    int ans = 0;
    for (int i = 1; i <= N; i++) {
        if (s[i] != i * s[N] / N) {
            ans++;
        }
    }

    cout << ans << endl;
}