#include <bits/stdc++.h>
using namespace std;

struct SegmentTree {
    const int N, n;
    vector<int> INF = {1 << 30, 1 << 30};
    vector<vector<int>> tree;

    SegmentTree(vector<vector<int>> A) : N(A.size()), n(bit_length(N-1)), tree(1 << (n+1), INF) {
        for (int i = 0; i < N; i++) {
            tree[(1 << n) + i] = A[i];
        }
        for (int pos = (1 << n) - 1; pos > 0; pos--) {
            tree[pos] = min(tree[pos << 1], tree[pos << 1 | 1]);
        }
    }

    int bit_length(int N) {
        int result = 0;
        while (N) {
            result++;
            N >>= 1;
        }
        return result;
    }

    vector<int> query(int l, int r) {
        // [l, r) (0 ≤ l < N, 1 ≤ r ≤ N)のminを求める
        l += 1 << n;
        r += 1 << n;
        vector<int> value_l = INF, value_r = INF;
        while (l != r) {
            if (l & 1 == 1) {
                value_l = min(value_l, tree[l]);
                l++;
            }
            if (r & 1 == 1) {
                r--;
                value_r = min(tree[r], value_r);
            }
            l >>= 1;
            r >>= 1;
        }
        return min(value_l, value_r);
    }
};

int main() {
    // 100点解法
    int N, x, y, Q, a, b;
    cin >> N;

    vector<vector<int>> g(N);
    for (int i = 0; i < N-1; i++) {
        cin >> x >> y;
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }


    vector<int> l(N, 0), r(N, 0), depth(N, 0);
    // depth[i] := iの、根からの深さ
    vector<vector<int>> tour;

    auto dfs = [&](auto&& self, int v, int p) -> void {
        l[v] = tour.size();
        tour.push_back({depth[v], v});
        for (int u : g[v]) {
            if (u == p) continue;

            depth[u] = depth[v] + 1;
            self(self, u, v);
            tour.push_back({depth[v], v});
        }
        r[v] = tour.size();
    };

    dfs(dfs, 0, -1);

    SegmentTree st(tour);


    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> a >> b;
        a--;
        b--;

        if (l[b] < l[a]) swap(a, b);

        int p = st.query(l[a], l[b] + 1)[1];
        cout << depth[a] + depth[b] - 2 * depth[p] + 1 << endl;
    }
}