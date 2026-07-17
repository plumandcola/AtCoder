#include <bits/stdc++.h>
using namespace std;

int dfs(int i, int N, const vector<unordered_set<int>>& g, vector<int> members) {
    if (i == N) return members.size();

    int result = dfs(i+1, N, g, members); // 議員iを含めない場合

    bool ok = true; // 議員iが、すでに派閥に含まれる議員の全員と仲が良いかを確認
    for (int j : members) {
        if (g[i].find(j) == g[i].end()) ok = false;
    }
    if (ok) {
        members.push_back(i);
        result = max(result, dfs(i+1, N, g, members)); // 議員iを含める場合
    }

    return result;
}

int main() {
    int N, M, x, y;
    cin >> N >> M;
    
    vector<unordered_set<int>> g(N, unordered_set<int>{});
    for (int i = 0; i < M; i++) {
        cin >> x >> y;
        g[x-1].insert(y-1);
        g[y-1].insert(x-1);
    }

    cout << dfs(0, N, g, {}) << endl;
}