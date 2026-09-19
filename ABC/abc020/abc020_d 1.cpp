#include <bits/stdc++.h>
using namespace std;

int main() {
    // 15点解法
    long long N, K, ans = 0;
    cin >> N >> K;

    for (int i = 1; i <= N; i++) {
        ans = (ans + lcm(i, K)) % 1000000007;
    }

    cout << ans << endl;
}