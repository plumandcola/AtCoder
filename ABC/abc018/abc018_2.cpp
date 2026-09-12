#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    int N, l, r;
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> l >> r;
        reverse(S.begin() + l - 1, S.begin() + r);
    }

    cout << S << endl;
}