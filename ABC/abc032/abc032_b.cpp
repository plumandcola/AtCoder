#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int k;
    cin >> s >> k;

    unordered_set<string> password;
    for (int i = 0; i + k <= s.size(); i++) {
        password.insert(s.substr(i, k));
    }

    cout << password.size() << endl;
}