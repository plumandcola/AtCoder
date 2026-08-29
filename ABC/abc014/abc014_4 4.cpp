#include <bits/stdc++.h>
using namespace std;

struct LCA {
    const int N, n;
    vector<vector<int>> parent;
    vector<int> dist;

    LCA(vector<vector<int>> g) : N(g.size()), n(bit_length(N-1)), parent(n, vector<int>(N, 0)), dist(N, -1) {
        dist[0] = 0;
        vector<int> q = {0};
        while (!q.empty()) {
            int v = q.back();
            q.pop_back();
            for (int u : g[v]) {
                if (dist[u] == -1) {
                    parent[0][u] = v;
                    dist[u] = dist[v] + 1;
                    q.push_back(u);
                }
            }
        }

        for (int k = 0; k < n-1; k++) {
            for (int i = 0; i < N; i++) {
                parent[k+1][i] = parent[k][parent[k][i]];
            }
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

    int query(int v, int u) {
        // vの方が深くなるようにする
        if (dist[v] < dist[u]) swap(v, u);

        // LCAまでの距離を同じにする
        int diff = dist[v] - dist[u];
        int k = 0;
        while (diff) {
            if (diff & 1) v = parent[k][v];
            diff >>= 1;
            k++;
        }

        // 二分探索でLCAを求める
        if (v == u) return v;
        for (int k = n-1; k >= 0; k--) {
            if (parent[k][v] != parent[k][u]) {
                v = parent[k][v];
                u = parent[k][u];
            }
        }
        return parent[0][v];
    }

    int get_dist(int v, int u) {
        return dist[v] + dist[u] - 2 * dist[query(v, u)];
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

    LCA tree(g);

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> a >> b;
        cout << tree.get_dist(a-1, b-1) + 1 << endl;;
    }
}