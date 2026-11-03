#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    long long N;
    cin >> N;
    vector<long long> a(N);
    for (long long i = 0; i < N; i++) cin >> a[i];

    long long ans = 0;
    long long l = 0;
    long long r = 1;
    while (l < N) {
        while (r < N && a[r] > a[r-1]) r++;
        ans += (r - l) * (r - l + 1) / 2;
        l = r;
        r++;
    }

    cout << ans << endl;
}