#include <bits/stdc++.h>
using namespace std;

int main() {
    string w;
    cin >> w;

    map<char, int> count;
    for (char c : w) count[c]++;

    for (char c = 'a'; c <= 'z'; c++) {
        if (count[c] % 2 == 1) {
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
}