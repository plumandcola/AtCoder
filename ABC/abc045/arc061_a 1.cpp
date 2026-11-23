#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;

    long long ans = 0;
    long long tmp = 0;
    int n = S.size();
    for (long long b = 0; b < (1 << (n-1)); b++) {
        for (long long i = 0; i < n; i++) {
            tmp += S[i] - '0';
            if ((b >> i) & 1) tmp *= 10;
            else {
                ans += tmp;
                tmp = 0;
            }
        }
    }

    cout << ans << endl;
}