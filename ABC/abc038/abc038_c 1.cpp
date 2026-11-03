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
    long long r = 0;
    while (l < N) {
        while (r < l || (r+1 < N && a[r+1] > a[r])) r++;
        ans += r - l + 1;
        l++;
    }

    cout << ans << endl;
}