#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, B, C, mod = 1000000007;
    cin >> A >> B >> C;

    cout << A * B % mod * C % mod << endl;
}