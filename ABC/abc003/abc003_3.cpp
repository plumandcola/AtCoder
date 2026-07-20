#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    
    vector<int> R(N);
    for (int i = 0; i < N; i++) cin >> R[i];
    sort(R.begin(), R.end());
    reverse(R.begin(), R.end());
    
    double ans = 0;
    for (int i = 0; i < K; i++) {
        double r = R[i];
        for (int j = 0; j < i + 1; j++) r /= 2.0;
        ans += r;
    }
    
    cout << fixed << setprecision(10) << ans << endl;
}