#include <bits/stdc++.h>
using namespace std;

int main() {
    // 100点解法
    int N, w, h;
    cin >> N;

    vector<vector<int>> boxes(N, vector<int>(2)); // wの昇順かつhの降順でソート
    for (int i = 0; i < N; i++) {
        cin >> w >> h;
        boxes[i][0] = w;
        boxes[i][1] = -h;
    }
    sort(boxes.begin(), boxes.end());

    vector<int> dp;
    for (int i = 0; i < N; i++) {
        w = boxes[i][0];
        h = -boxes[i][1]; // hの符号を反転させているので、元に戻す
        auto it = lower_bound(dp.begin(), dp.end(), h);
        if (it == dp.end()) dp.push_back(h);
        else *it = h;
    }

    cout << dp.size() << endl;
}