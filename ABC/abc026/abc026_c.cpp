#include <bits/stdc++.h>
using namespace std;

void dfs(int v, vector<vector<int>>& g, vector<int>& salaries) {
    // 直属の部下がいない場合
    if (g[v].size() == 0) salaries[v] = 1;

    // 直属の部下がいる場合
    else {
        int M = 0; // max
        int m = 1 << 30; // min
        for (int u : g[v]) {
            dfs(u, g, salaries);

            M = max(M, salaries[u]);
            m = min(m, salaries[u]);

            salaries[v] = M + m + 1;
        }
    }
}

int main() {
    int N, B;
    cin >> N;

    vector<vector<int>> g(N, vector<int> (0));
    for (int i = 1; i < N; i++) {
        cin >> B;
        g[B-1].push_back(i);
    }

    vector<int> salaries(N, -1); // salaries[i] := 社員番号がiの社員の給料

    dfs(0, g, salaries);

    cout << salaries[0] << endl;
}