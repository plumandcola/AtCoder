#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, sum = 0;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        sum += a[i];
    }

    if (sum % N != 0) {
        cout << -1 << endl;
        return 0;
    }

    int ans = N, ave = sum / N, s = 0, n = 0;
    for (int i = 0; i < N; i++) {
        s += a[i];
        n++;
        if (s == ave * n) { // ここまでの島に橋を架ける
            s = 0;
            n = 0;
            ans--;
        }
    }

    cout << ans << endl;
}