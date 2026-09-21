#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, ans = 0;
    cin >> N;
    vector<bool> visited(100000, false);
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (visited[A-1] == false) visited[A-1] = true;
        else ans++;
    }

    cout << ans << endl;
}