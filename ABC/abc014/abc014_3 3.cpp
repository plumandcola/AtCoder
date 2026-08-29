#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int n, a, b;
    cin >> n;

    vector<pair<int, int>> query;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        query.push_back({a, 1});
        query.push_back({b+1, -1});
    }
    sort(query.begin(), query.end());

    // イベントソート(?)
    int num = 0; // 人気
    map<int, int> s;
    for (auto [color, change] : query) {
        num += change;
        s[color] = num;
    }

    int ans = -1;
    for (auto [color, num] : s) {
        if (num > ans) ans = num;
    }

    cout << ans << endl;
}