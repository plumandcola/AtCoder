#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, ans = "";
    cin >> s;

    int n = s.size(), l = 0, r = 0;
    while (l < n) {
        while (r < n && s[l] == s[r]) r++;
        cout << s[l] << r - l;
        l = r;
    }

    cout << endl;
}