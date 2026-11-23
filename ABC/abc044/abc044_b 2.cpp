#include <bits/stdc++.h>
using namespace std;

int main() {
    string w;
    cin >> w;

    map<int, int> count;
    for (char c : w) count[c - 'a']++;

    for (int i = 0; i < 26; i++) {
        if (count[i] % 2 == 1) {
            cout << "No" << endl;
            return 0;
        }
    }

    cout << "Yes" << endl;
}