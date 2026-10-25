#include <bits/stdc++.h>
using namespace std;

using pii = pair<int, int>;

int main() {
    int N, M, a, b, t, INF = 1 << 30;
    cin >> N >> M;

    vector<vector<pii>> g(N);
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> t;
        g[a-1].push_back({b-1, t});
        g[b-1].push_back({a-1, t});
    }

    int ans = INF;
    for (int i = 0; i < N; i++) { // i番目のバス停に引っ越した際
        // ダイクストラ法
        vector<int> time(N, INF);
        time[i] = 0;
        priority_queue<pii, vector<pii>, greater<pii>> q;
        q.push({0, i});
        while (!q.empty()) {
            auto [T, v] = q.top();
            q.pop();
            if (time[v] < T) continue;

            for (auto [u, t] : g[v]) {
                int T_new = T + t;
                if (time[u] > T_new) {
                    q.push({T_new, u});
                    time[u] = T_new;
                }
            }
        }
        ans = min(ans, *max_element(time.begin(), time.end()));
    }

    cout << ans << endl;
}