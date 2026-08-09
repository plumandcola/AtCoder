#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N;
    cin >> N;
    vector<int> C(N);
    for (int i = 0; i < N; i++) cin >> C[i];
    
    double ans = 0;
    for (int i = 0; i < N; i++) {
        int count = 0; // C[j](0≤j<N,j≠i)のうち、C[i]の約数の個数
        for (int j = 0; j < N; j++) {
            if (C[i] % C[j] == 0 && i != j) count++;
        }

        ans += (count / 2 + 1.0) / (count + 1.0);
    }

    cout << fixed << setprecision(10) << ans << endl;
}