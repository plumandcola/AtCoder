#include <bits/stdc++.h>
using namespace std;

int main() {
    string W, ans = "";
    cin >> W;
    for (char c : W) {
        if (c != 'a' && c != 'i' && c != 'u' && c != 'e' && c != 'o') ans += c;
    }
    cout << ans << endl;
}