#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int n, a, b;
    cin >> n;

    vector<int> ans(1000001, 0);
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        for (int j = a; j <= b; j++) ans[j]++;
    }

    cout << *max_element(ans.begin(), ans.end()) << endl;
}