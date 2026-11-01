#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    set<int> b;
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        b.insert(a[i]);
    }

    map<int, int> ans;
    int i = 0;
    for (int n : b) {
        ans[n] = i;
        i++;
    }

    for (int i = 0; i < N; i++) cout << ans[a[i]] << endl;
}