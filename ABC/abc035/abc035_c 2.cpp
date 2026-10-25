#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, Q, l, r;
    cin >> N >> Q;

    vector<int> board(N+1, 0); // いもす法

    for (int i = 0; i < Q; i++) {
        cin >> l >> r;
        board[l-1]++;
        board[r]--;
    }

    for (int i = 0; i < N; i++) {
        cout << board[i] % 2;
        board[i+1] += board[i];
    }
    cout << endl;
}