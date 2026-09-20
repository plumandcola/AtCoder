#include <bits/stdc++.h>
using namespace std;

int main() {
    // 99点解法
    int n, k;
    cin >> n >> k;

    vector<long long> ans(n+1, 0); // ans[k][i] := 1 ≤ a_1 ≤ ... ≤ a_k ≤ i を満たす整数の組aの個数(累積和) → 二次元を一次元にしたもの
    ans[1] = 1;
    for (int i = 0; i <= k; i++) {
        for (int j = 0; j < n; j++) {
            ans[j+1] = (ans[j+1] + ans[j]) % 1000000007;
        }
    }

    cout << ans[n] << endl;
}