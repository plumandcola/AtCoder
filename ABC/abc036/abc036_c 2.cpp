#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    vector<int> b(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        b[i] = a[i];
    }

    sort(b.begin(), b.end());
    b.erase(unique(b.begin(), b.end()), b.end());

    for (int i = 0; i < N; i++) {
        cout << lower_bound(b.begin(), b.end(), a[i]) - b.begin() << endl;
    }
}