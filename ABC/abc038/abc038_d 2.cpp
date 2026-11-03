#include <bits/stdc++.h>
using namespace std;

struct BIT {
    const int n;
    vector<int> Tree;

    BIT(int n) : n(n), Tree(n+1, 0) {}

    void update(int i, int x) { // A[i]をxに更新する
        while (i <= n) {
            Tree[i] = max(Tree[i], x);
            i += i & -i;
        }
    }

    int query(int i) { // A[i]までの最大値を計算
        int ans = 0;
        while (i > 0) {
            ans = max(ans, Tree[i]);
            i -= i & -i;
        }
        return ans;
    }
};

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

    vector<int> dp(100001, 0); // dp[h] := 最も外側の箱の縦がh cmのときに、最大で何重の入れ子にできるか
    BIT bit(100001);
    for (int i = 0; i < N; i++) {
        w = boxes[i][0];
        h = -boxes[i][1]; // hの符号を反転させているので、元に戻す
        dp[h] = max(dp[h], bit.query(h-1) + 1);
        bit.update(h, dp[h]);
    }

    cout << *max_element(dp.begin(), dp.end()) << endl;
}