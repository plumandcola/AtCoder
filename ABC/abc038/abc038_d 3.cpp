#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    const int N, n, size;
    vector<int> tree;

    SegmentTree(int N) : N(N), n(bit_length(N-1)), size(1 << n), tree(size << 1, 0) {}

    int bit_length(int N) {
        int result = 0;
        while (N) {
            result++;
            N >>= 1;
        }
        return result;
    }

    void update(int pos, int x) {
        // pos (0 ≤ pos < N)番目の値をxに更新
        pos += size;
        tree[pos] = x;
        pos >>= 1;
        while (pos > 0) {
            tree[pos] = max(tree[pos << 1], tree[pos << 1 | 1]);
            pos >>= 1;
        }
    }

    int query(int l, int r) {
        // [l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のmaxを求める
        l += size;
        r += size;
        int value_l = 0, value_r = 0;
        while (l != r) {
            if (l & 1) {
                value_l = max(value_l, tree[l]);
                l++;
            }
            if (r & 1) {
                r--;
                value_r = max(tree[r], value_r);
            }
            l >>= 1;
            r >>= 1;
        }
        return max(value_l, value_r);
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
    SegmentTree st(100001);
    for (int i = 0; i < N; i++) {
        w = boxes[i][0];
        h = -boxes[i][1]; // hの符号を反転させているので、元に戻す
        dp[h] = max(dp[h], st.query(0, h) + 1);
        st.update(h, dp[h]);
    }

    cout << *max_element(dp.begin(), dp.end()) << endl;
}