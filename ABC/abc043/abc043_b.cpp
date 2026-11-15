#include <bits/stdc++.h>
using namespace std;

int main() {
    string s, ans = "";
    cin >> s;

    for (char c : s) {
        if (c == '0' || c == '1') ans += c;
        else if (c == 'B' && ans.size()) ans.pop_back();
    }

    cout << ans << endl;
}