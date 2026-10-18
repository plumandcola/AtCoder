#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    S += "+";

    int ans = 0;
    bool contains_0 = false;
    for (char c : S) {
        if (c == '0') {
            contains_0 = true;
        } else if (c == '+') {
            if (contains_0 == false) ans++;
            else contains_0 = false;
        }
    }

    cout << ans << endl;
}