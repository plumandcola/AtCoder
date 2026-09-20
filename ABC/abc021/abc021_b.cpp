#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, a, b, K, P;
    cin >> N >> a >> b >> K;

    vector<bool> visited(N+1, false);
    visited[a] = true;
    visited[b] = true;

    string ans = "YES";
    for (int i = 0; i < K; i++) {
        cin >> P;
        if (visited[P] == true) ans = "NO";
        else visited[P] = true;
    }
    cout << ans << endl;
}