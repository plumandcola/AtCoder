#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    cout << s.size() / 2 - count(s.begin(), s.end(), 'p') << endl;
}