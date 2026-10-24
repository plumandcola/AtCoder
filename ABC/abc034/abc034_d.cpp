#include <bits/stdc++.h>
using namespace std;

bool judge(int& N, int& K, vector<long long>& w, vector<long long>& p, long double& mid) {
    vector<long double> y(N);
    for (int i = 0; i < N; i++) y[i] = p[i] * w[i] - mid * w[i];
    sort(y.begin(), y.end(), greater<long double>{});
    long double sum = 0;
    for (int i = 0; i < K; i++) sum += y[i];
    return sum >= 0;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<long long> w(N), p(N);
    for (int i = 0; i < N; i++) cin >> w[i] >> p[i];

    // 二分探索
    long double l = 0.0;
    long double r = 10000.0;
    while (abs(r - l) > 0.0000000001) {
        long double mid = (l + r) / 2;
        if (judge(N, K, w, p, mid)) {
            l = mid;
        } else {
            r = mid;
        }
    }

    cout << fixed << setprecision(15) << l << endl;
}