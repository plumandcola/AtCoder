#include <bits/stdc++.h>
using namespace std;

void dfs(int v, int w, vector<bool>& visited, const auto& g) {
    for (auto [u, y] : g[v]) {
        if (y > w && visited[u] == false) {
            visited[u] = true;
            dfs(u, w, visited, g);
        }
    }
}

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
        cin >> v >> w;
        vector<bool> visited(N, false);
        visited[v-1] = true;
        dfs(v-1, w, visited, g); // dfs(再帰)
        int ans = 0;
        for (int i = 0; i < N; i++) ans += visited[i];
        cout << ans << endl;
    }
}