#include <bits/stdc++.h>
using namespace std;

using tlll = tuple<long long, long long, long long>;

const long long INF = 1LL << 61;
const vector<pair<long long, long long>> moves = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool bfs(const vector<string>& s, const long long& H, const long long& W, const long long& si, const long long& sj, const long long& gi, const long long& gj, const long long& x, const long long& T) {
    vector<vector<long long>> d(H, vector<long long>(W, INF));
    priority_queue<tlll, vector<tlll>, greater<tlll>> q;
    q.push({0, si, sj});
    while (!q.empty()) {
        auto [t, i, j] = q.top();
        q.pop();
        if (d[i][j] != INF) continue; // すでに探索済み

        d[i][j] = t;
        for (auto [di, dj] : moves) {
            long long ni = i + di, nj = j + dj;
            if (ni < 0 || ni >= H || nj < 0 || nj >= W || d[ni][nj] != INF) continue;

            if (s[ni][nj] != '#') q.push({t + 1, ni, nj});
            else if (s[ni][nj] == '#') q.push({t + x, ni, nj});
        }
    }

    return d[gi][gj] <= T;
}

int main() {
    long long H, W, T;
    cin >> H >> W >> T;
    vector<string> s(H);
    for (int i = 0; i < H; i++) cin >> s[i];

    long long si, sj, gi, gj;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (s[i][j] == 'S') {
                si = i;
                sj = j;
            } else if (s[i][j] == 'G') {
                gi = i;
                gj = j;
            }
        }
    }

    long long l = 0, r = T;
    while (r - l > 1) {
        long long mid = (l + r) / 2;
        if (bfs(s, H, W, si, sj, gi, gj, mid, T)) l = mid;
        // ↑T秒以内にゴール地点に到着することが可能
        else r = mid;
    }

    cout << l << endl;
}