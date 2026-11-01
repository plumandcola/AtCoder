#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;
    vector<long long> a(N);
    for (long long i = 0; i < N; i++) cin >> a[i];

    long long ans = 0;
    for (long long i = 0; i < N-K+1; i++) {
        for (long long j = 0; j < K; j++) {
            ans += a[i+j];
        }
    }

    cout << ans << endl;
}