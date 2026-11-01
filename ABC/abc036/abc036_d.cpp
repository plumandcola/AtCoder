#include <bits/stdc++.h>
using namespace std;

void dfs(long long v, long long p, vector<long long>& dp_w, vector<long long>& dp_b, vector<vector<long long>>& g, long long& mod) {
    for (long long u : g[v]) {
        if (u == p) continue;

        dfs(u, v, dp_w, dp_b, g, mod);
        dp_w[v] = dp_w[v] * (dp_w[u] + dp_b[u]) % mod;
        dp_b[v] = dp_b[v] * dp_w[u] % mod;
    }
}

int main() {
    long long N, a, b, mod = 1000000007;
    cin >> N;

    vector<vector<long long>> g(N);
    for (long long i = 0; i < N-1; i++) {
        cin >> a >> b;
        g[a-1].push_back(b-1);
        g[b-1].push_back(a-1);
    }

    vector<long long> dp_w(N, 1);
    // dp_w[v] := 島vが白で塗られる、色の塗り方
    vector<long long> dp_b(N, 1);
    // dp_b[v] := 島vが黒で塗られる、色の塗り方

    dfs(0, -1, dp_w, dp_b, g, mod);

    cout << (dp_w[0] + dp_b[0]) % mod << endl;
}