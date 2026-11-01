#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<long long> a(N);
    for (long long i = 0; i < N; i++) cin >> a[i];

    long long ans = 0;
    for (long long i = 0; i < N; i++) {
        ans += a[i] * min({i+1, K, N-K+1, N-i});
    }

    cout << ans << endl;
}