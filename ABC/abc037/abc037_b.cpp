#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Q, L, R, T;
    cin >> N >> Q;
    vector<int> a(N, 0);

    for (int i = 0; i < Q; i++) {
        cin >> L >> R >> T;
        for (int j = L-1; j < R; j++) a[j] = T;
    }

    for (int i = 0; i < N; i++) cout << a[i] << endl;
}