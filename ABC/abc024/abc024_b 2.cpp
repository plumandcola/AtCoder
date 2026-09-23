#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int max_t = 1100001, N, T, a, ans = 0;
    set<int> A;
    vector<int> close(max_t, 0); // close[i] := 時刻iの時点でドアが何秒後に閉まる予定か？

    cin >> N >> T;
    for (int i = 0; i < N; i++) {
        cin >> a;
        A.insert(a);
    }

    for (int t = 1; t < max_t; t++) {
        if (A.find(t) != A.end()) close[t] = T;
        else close[t] = max(0, close[t-1] - 1);

        ans += (close[t] > 0);
    }
    cout << ans << endl;
}