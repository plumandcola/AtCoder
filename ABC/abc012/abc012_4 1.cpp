#include <bits/stdc++.h>
using namespace std;

using pii = pair<int, int>;

int main() {
    int N, M, a, b, t;
    cin >> N >> M;

    vector<vector<pii>> g(N);
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> t;
        g[a-1].push_back({b-1, t});
        g[b-1].push_back({a-1, t});
    }

    int ans = 1 << 30;
    for (int i = 0; i < N; i++) { // i番目のバス停に引っ越した際
        vector<int> time(N, -1);
        priority_queue<pii, vector<pii>, greater<pii>> q;
        q.push({0, i});
        while (!q.empty()) {
            int T = q.top().first;
            int v = q.top().second;
            q.pop();
            if (time[v] != -1) continue;

            time[v] = T;
            for (int j = 0; j < g[v].size(); j++) {
                int u = g[v][j].first;
                int t = g[v][j].second;
                if (time[u] == -1) q.push({T + t, u});
            }
        }
        ans = min(ans, *max_element(time.begin(), time.end()));
    }

    cout << ans << endl;
}