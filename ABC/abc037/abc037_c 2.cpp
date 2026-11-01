#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<long long> a(N);
    for (long long i = 0; i < N; i++) cin >> a[i];

    vector<long long> s(N+1, 0); // 累積和
    for (long long i = 0; i < N; i++) s[i+1] = s[i] + a[i];

    long long ans = 0;
    for (long long i = 0; i < N-K+1; i++) {
        ans += s[i+K] - s[i];
    }

    cout << ans << endl;
}