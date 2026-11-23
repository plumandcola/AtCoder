#include <bits/stdc++.h>
using namespace std;

long long pow(long long a, long long b) {
    // aのb乗を求める
    long long result = 1;
    for (long long i = 0; i < b; i++) result *= a;

    return result;
}

int main() {
    string S;
    cin >> S;

    long long ans = 0;
    int n = S.size();

    for (long long i = 0; i < n; i++) {
        long long ans_i = pow(10, n-i-1); // "+"がないときの数字

        if (i < n-1) ans_i += pow(2, n-i-2) * (pow(5, n-i-1) - 1) / 4;
        // 後ろの"+"の有無や桁数などを考慮して導かれた等比数列の和 2^(n-i-2) * (5^(n-i-1) - 1) / 4

        ans_i *= (S[i] - '0') * pow(2, i);
        // i+1文字目の数字 × それまでの"+"の有無

        ans += ans_i;
    }

    cout << ans << endl;
}