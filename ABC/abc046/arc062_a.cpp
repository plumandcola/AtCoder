#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, T, A;
    cin >> N;

    vector<long long> ans(2, 1);
    for (long long i = 0; i < N; i++) {
        cin >> T >> A;
        long long r = max((ans[0] + T - 1) / T, (ans[1] + A - 1) / A);
        ans = {r * T, r * A};
    }

    cout << ans[0] + ans[1] << endl;
}