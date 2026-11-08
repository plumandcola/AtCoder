#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, a;
    cin >> N;
    vector<pair<int, int>> ans;
    for (int i = 1; i <= N; i++) {
        cin >> a;
        ans.push_back({a, i});
    }

    sort(ans.begin(), ans.end(), greater<>());

    for (auto [a, i] : ans) {
        cout << i << endl;
    }
}