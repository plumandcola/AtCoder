#include <bits/stdc++.h>
using namespace std;

using pll = pair<long long, long long>;

int main() {
    long long N, M, T, a, b, c, INF = 1LL << 62;
    cin >> N >> M >> T;
    vector<long long> A(N);
    for (long long i = 0; i < N; i++) cin >> A[i];

    vector<vector<pll>> g(N);
    vector<vector<pll>> g_r(N); // 逆向き
    for (long long i = 0; i < M; i++) {
        cin >> a >> b >> c;
        g[a-1].push_back({b-1, c});
        g_r[b-1].push_back({a-1, c});
    }

    auto dijkstra = [&](const vector<vector<pll>>& g) -> vector<long long> {
        vector<long long> d(N, INF);
        d[0] = 0;
        priority_queue<pll, vector<pll>, greater<pll>> q;
        q.push({0, 0});
        while (!q.empty()) {
            auto [C, v] = q.top();
            q.pop();
            if (d[v] < C) continue;

            for (auto [u, c] : g[v]) {
                long long C_new = C + c;
                if (d[u] > C_new) {
                    q.push({C_new, u});
                    d[u] = C_new;
                }
            }
        }
        return d;
    };

    // ダイクストラ法
    vector<long long> d = dijkstra(g);
    vector<long long> d_r = dijkstra(g_r); // 逆向き

    long long ans = 0;
    for (long long i = 0; i < N; i++) {
        if (d[i] != INF && d_r[i] != INF && d[i] + d_r[i] <= T) {
            ans = max(ans, A[i] * (T - d[i] - d_r [i]));
        }
    }

    cout << ans << endl;
}