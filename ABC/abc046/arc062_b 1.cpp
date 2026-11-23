#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;

    int n = s.size();
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            if (s[i] == 'p') ans--;
        } else if (i % 2 == 1) {
            if (s[i] == 'g') ans++;
        }
    }

    cout << ans << endl;
}