#include <bits/stdc++.h>
using namespace std;

int main() {
    // 200点解法
    string s;
    cin >> s;
    int n = s.size();

    int l = -1;
    int r = -1;
    for (int i = 0; i < n-1; i++) {
        for (int j = i+1; j < n; j++) {
            map<char, int> count;
            for (int k = i; k <= j; k++) count[s[k]]++;
            for (auto [c, m] : count) {
                if (m > (j - i + 1) / 2) {
                    l = i+1;
                    r = j+1;
                }
            }
        }
    }

    cout << l << " " << r << endl;
}