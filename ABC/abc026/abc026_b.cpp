#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans = 0;
    cin >> N;
    vector<int> R(N);
    for (int i = 0; i < N; i++) cin >> R[i];

    sort(R.begin(), R.end());
    reverse(R.begin(), R.end());

    for (int i = 0; i < N; i++) {
        if (i % 2 == 0) ans += R[i] * R[i];
        else ans -= R[i] * R[i];
    }

    cout << fixed << setprecision(15) << ans * numbers::pi << endl;
}