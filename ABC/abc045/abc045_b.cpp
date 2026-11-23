#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<string> S(3);
    for (int i = 0; i < 3; i++) cin >> S[i];

    int turn = 0;
    vector<int> index(3, 0);
    while (true) {
        if (index[turn] < S[turn].size()) {
            char next = S[turn][index[turn]];
            index[turn]++;
            turn = next - 'a';
        } else {
            cout << char('A' + turn) << endl;
            break;
        }
    }
}