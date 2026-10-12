#include <bits/stdc++.h>
using namespace std;

int main() {
    int L, H, N, A;
    cin >> L >> H >> N;
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (A > H) cout << -1 << endl;
        else if (L <= A && A <= H) cout << 0 << endl;
        else cout << L - A << endl;
    }
}