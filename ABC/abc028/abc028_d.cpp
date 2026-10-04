#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K;
    cin >> N >> K;

    long double ans = 0.0;

    // 3回とも異なる数字が出る場合
    ans += (K-1) * (N-K) * 6;

    // 2回Kが出る場合
    ans += (N-1) * 3;

    // 3回ともKが出る場合
    ans += 1;

    cout << fixed << setprecision(15) << ans / N / N / N << endl;
}