#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    vector<int> dp(N, 1 << 30);
    dp[0] = 0;
    for (int i = 0; i < N-1; i++) {
        dp[i+1] = min(dp[i+1], dp[i] + abs(a[i+1] - a[i]));
        if (i+2 < N) dp[i+2] = min(dp[i+2], dp[i] + abs(a[i+2] - a[i]));
    }

    cout << dp[N-1] << endl;
}