#include <bits/stdc++.h>
using namespace std;

void dfs(int v, vector<vector<int>>& g, vector<int>& d) {
    for (int u : g[v]) {
        if (d[u] == -1) {
            d[u] = d[v] + 1;
            dfs(u, g, d);
        }
    }
}

int main() {
    // 30点解法
    int N, x, y, Q, a, b;
    cin >> N;

    vector<vector<int>> g(N);
    for (int i = 0; i < N-1; i++) {
        cin >> x >> y;
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        cin >> a >> b;
        vector<int> d(N, -1);
        d[a-1] = 0;
        dfs(a-1, g, d); // dfs(再帰)
        cout << d[b-1] + 1 << endl;
    }
}