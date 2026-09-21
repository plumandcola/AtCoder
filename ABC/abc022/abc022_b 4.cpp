#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, ans = 0;
    cin >> N;

    vector<int> flowers;
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (find(flowers.begin(), flowers.end(), A) != flowers.end()) ans++;
        else flowers.push_back(A);
    }

    cout << ans << endl;
}