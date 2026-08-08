#include <bits/stdc++.h>
using namespace std;
using vll = vector<long long>;

long long count(long long N) {
    // N以下の数字のうち、4か9が含まれている数字の個数
    string N_str = to_string(N);
    long long n = N_str.size();
    vector<vector<vll>> dp(n+1, vector<vll>(2, vll(2, 0)));
    // dp[i][b1][b2], b2: 4か9が含まれているかどうか
    dp[0][0][0] = 1;

    for (long long i = 0; i < n; i++) {
        for (long long b1 = 0; b1 < 2; b1++) {
            long long limit = b1 == 1 ? 9 : N_str[i] - '0';
            for (long long b2 = 0; b2 < 2; b2++) {
                for (long long d = 0; d <= limit; d++) {
                    long long B1 = b1 | (d < N_str[i] - '0');
                    long long B2 = b2 | (d == 4) | (d == 9);
                    dp[i+1][B1][B2] += dp[i][b1][b2];
                }
            }
        }
    }

    return dp[n][0][1] + dp[n][1][1];
}

int main() {
    // 100点解法
    long long A, B;
    cin >> A >> B;

    cout << count(B) - count(A-1) << endl;
}