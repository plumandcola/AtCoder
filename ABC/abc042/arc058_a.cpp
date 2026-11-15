#include <bits/stdc++.h>
using namespace std;

bool check(int n, vector<bool>& D) {
    while (n) {
        if (D[n % 10] == true) return false;
        n /= 10;
    }
    return true;
}

int main() {
    int N, K, d;
    cin >> N >> K;
    vector<bool> D(10, false);
    for (int i = 0; i < K; i++) {
        cin >> d;
        D[d] = true;
    }

    int ans = N;
    while (check(ans, D) == false) {
        ans++;
    }

    cout << ans << endl;
}