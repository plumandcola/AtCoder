#include <bits/stdc++.h>
using namespace std;

int main() {
    int ans = 0;
    string S;
    for (int i = 0; i < 12; i++) {
        cin >> S;
        ans += (find(S.begin(), S.end(), 'r') != S.end());
    }

    cout << ans << endl;
}