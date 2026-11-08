#include <bits/stdc++.h>
using namespace std;

int main() {
    // 50点解法
    int N, M, a, b, y, Q, v, w;
    cin >> N >> M;
    vector<vector<pair<int, int>>> g(N, vector<pair<int, int>> (0));
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> y;
        g[a-1].push_back({b-1, y});
        g[b-1].push_back({a-1, y});
    }

    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int ans = 1;
        cin >> v >> w;
        vector<int> q = {v-1}; // dfs(スタック)
        vector<bool> visited(N, false);
        visited[v-1] = true;
        while (!q.empty()) {
            int v = q.back();
            q.pop_back();
            for (auto [u, y] : g[v]) {
                if (y > w && visited[u] == false) {
                    visited[u] = true;
                    ans++;
                    q.push_back(u);
                }
            }
        }
        cout << ans << endl;
    }
}