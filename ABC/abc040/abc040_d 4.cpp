#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<int> parent; // 各要素の親要素の番号を格納するリスト、要素が根（ルート）の場合は-(そのグループの要素数)を格納する

    UnionFind(int n) : parent(n, -1) {}

    int find(int x) { // 要素xが属するグループの根を返す
        if (parent[x] < 0) return x; // 根
        return parent[x] = find(parent[x]); // 経路圧縮
    }

    void unite(int x, int y) { // 要素xが属するグループと要素yが属するグループとを併合する
        x = find(x);
        y = find(y);

        if (x == y) return;

        if (parent[x] > parent[y]) swap(x, y);

        parent[x] += parent[y];
        parent[y] = x;
    }

    int size(int x) { // 要素xが属するグループのサイズ（要素数）を返す
        return -parent[find(x)];
    }
};

int main() {
    // 100点解法
    vector<vector<int>> q;

    int N, M, a, b, y, Q, v, w;
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> y;
        q.push_back({y, -1, a-1, b-1}); // -1は、クエリでないことを表す
    }

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> v >> w;
        q.push_back({w, i, v-1, -1});
    }

    sort(q.rbegin(), q.rend()); // 年の降順にソート

    vector<int> ans(Q);
    UnionFind uf(N);

    for (vector<int> query : q) {
        if (query[1] == -1) { // 道路を使えるようにする
            int a = query[2];
            int b = query[3];
            uf.unite(a, b);
        } else { // クエリ
            int i = query[1];
            int v = query[2];
            ans[i] = uf.size(v);
        }
    }

    for (int i = 0; i < Q; i++) {
        cout << ans[i] << endl;
    }
}