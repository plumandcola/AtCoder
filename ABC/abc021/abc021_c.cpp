#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, a, b, M, x, y, mod = 1000000007;
    cin >> N >> a >> b >> M;
    vector<vector<int>> g(N, vector<int>(0));
    for (int i = 0; i < M; i++) {
        cin >> x >> y;
        g[x-1].push_back(y-1);
        g[y-1].push_back(x-1);
    }

    vector<int> ans(N, 0);
    ans[a-1] = 1;
    vector<int> d(N, -1);
    d[a-1] = 0;
    deque<int> q;
    q.push_back(a-1);
    while (!q.empty()) {
        int v = q.front();
        q.pop_front();
        for (int u : g[v]) {
            if (d[u] == -1) {
                d[u] = d[v] + 1;
                ans[u] = (ans[u] + ans[v]) % mod;
                q.push_back(u);
            } else if (d[u] == d[v] + 1) {
                ans[u] = (ans[u] + ans[v]) % mod;
            }
        }
    }

    cout << ans[b-1] << endl;
}