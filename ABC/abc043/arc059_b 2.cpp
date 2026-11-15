#include <bits/stdc++.h>
using namespace std;

int main() {
    // 400点解法
    string s;
    cin >> s;
    int n = s.size();

    int l = -1;
    int r = -1;
    if (n == 2) {
        if (s[0] == s[1]) {
            l = 1;
            r = 2;
        }
    } else {
        for (int i = 0; i < n-2; i++) {
            map<char, int> count;
            for (int j = i; j <= i+2; j++) count[s[j]]++;
            for (auto [c, m] : count) {
                if (m >= 2) {
                    l = i+1;
                    r = i+3;
                }
            }
        }
    }

    cout << l << " " << r << endl;
}