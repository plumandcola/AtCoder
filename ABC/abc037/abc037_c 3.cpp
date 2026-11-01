#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<long long> a(N);
    for (long long i = 0; i < N; i++) cin >> a[i];

    long long s = 0;
    for (long long i = 0; i < K; i++) s += a[i];
    long long ans = s;
    for (long long i = 0; i < N-K; i++) {
        s -= a[i];
        s += a[i+K];
        ans += s;
    }

    cout << ans << endl;
}