#include <bits/stdc++.h>
using namespace std;

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


    vector<int> parent(N, 0), depth(N, 0), size(N, 1);
    // size := 部分木の大きさ

    // dfs 1回目 部分木の大きさを求め、heacy childを求める
    auto dfs1 = [&](auto&& self, int v, int p) -> void {
        if (g[v].size() >= 2 && g[v][0] == p) {
            swap(g[v].front(), g[v].back()); // vの親はg[v]の2番目以降へ
        }
        for (int i = 0; i < g[v].size(); i++) {
            int u = g[v][i];
            if (u == p) continue;
            parent[u] = v;
            depth[u] = depth[v] + 1;
            self(self, u, v);
            size[v] += size[u];
            if (size[u] > size[g[v][0]]) {
                swap(g[v][0], g[v][i]); // heavy childを、g[v]の先頭へ
            }
        }
    };

    dfs1(dfs1, 0, -1);


    int k = 1;
    vector<int> head(N, 0), id(N, 0)/* , vertex(N, 0) */;
    // head[v] := vを通るheavy pathの先頭（最も根側にある頂点）
    // id[v] := 行きがけ順で何番目にvを訪れるか
    // vertex[i] := 行きがけ順でi番目に訪れる頂点

    // dfs 2回目
    auto dfs2 = [&](auto&& self, int v, int p) -> void {
        for (int u : g[v]) {
            if (u == p) continue;

            head[u] = (u == g[v][0] ? head[v] : u); // uがvのheavy childならhead[u] = head[v]、そうでないならhead[u] = u
            id[u] = k;
            // vertex[k] = u;
            k++;
            self(self, u, v);
        }
    };

    dfs2(dfs2, 0, -1);


    auto LCA = [&](int a, int b) -> int {
        while (head[a] != head[b]) {
            if (id[a] > id[b]) swap(a, b);
            b = parent[head[b]];
        }
        return (id[a] < id[b] ? a : b);
    };


    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> a >> b;
        a--;
        b--;
        int p = LCA(a, b);

        cout << (depth[a] - depth[p]) + (depth[b] - depth[p]) + 1 << endl;
    }
}