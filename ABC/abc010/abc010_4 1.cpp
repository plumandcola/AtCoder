#include <bits/stdc++.h>
using namespace std;

int main() {
    // 99点解法
    int N, G, E;
    cin >> N >> G >> E;

    vector<int> p(G);
    for (int i = 0; i < G; i++) cin >> p[i];

    vector<vector<int>> friends(E, vector<int>(2));
    for (int i = 0; i < E; i++) cin >> friends[i][0] >> friends[i][1];

    int ans = N - 1;
    for (int i = 0; i < (1 << E); i++) { // bit全探索
        int ans_i = 0;
        vector<bool> trackable(N, false); // 高橋君が辿ることが可能かどうか
        vector<vector<int>> g(N, vector<int>(0));
        for (int j = 0; j < E; j++) {
            if ((i >> j) & 1 == 1) ans_i++; // 二人の友人関係を解消する
            else { // 二人の友人関係はそのまま
                int a = friends[j][0];
                int b = friends[j][1];
                g[a].push_back(b);
                g[b].push_back(a);
            }
        }

        deque<int> q = {0}; // bfs
        while (!q.empty()) {
            int v = q.front();
            q.pop_front();
            for (int u : g[v]) {
                if (trackable[u] == false) {
                    trackable[u] = true;
                    q.push_back(u);
                }
            }
        }

        for (int j = 0; j < G; j++) {
            if (trackable[p[j]] == true) ans_i++; // パスワードを変え、ログイン出来なくする
        }

        ans = min(ans, ans_i);
    }

    cout << ans << endl;
}