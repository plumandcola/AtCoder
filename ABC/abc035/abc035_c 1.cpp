#include <bits/stdc++.h>
using namespace std;

int main() {
    // 60点解法
    int N, Q, l, r;
    cin >> N >> Q;

    vector<int> board(N, 0);

    for (int i = 0; i < Q; i++) {
        cin >> l >> r;
        for (int j = l-1; j < r; j++) {
            board[j] ^= 1;
        }
    }

    for (int i = 0; i < N; i++) {
        cout << board[i];
    }
    cout << endl;
}