#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, ans = 0;
    cin >> N;

    set<int> flowers;
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (flowers.find(A) != flowers.end()) ans++;
        else flowers.insert(A);
    }

    cout << ans << endl;
}