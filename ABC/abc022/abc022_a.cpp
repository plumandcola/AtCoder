#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, S, T, A, W = 0, ans = 0;
    cin >> N >> S >> T;
    for (int i = 0; i < N; i++) {
        cin >> A;
        W += A;
        if (S <= W && W <= T) ans++;
    }

    cout << ans << endl;
}