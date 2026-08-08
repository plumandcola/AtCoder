#include <bits/stdc++.h>
using namespace std;

int main() {
    int R, C, sy, sx, gy, gx, y, x;
    cin >> R >> C >> sy >> sx >> gy >> gx;
    
    vector<string> c(R);
    for (int i = 0; i < R; i++) cin >> c[i];
    
    deque<int> q;
    q.push_back((sy - 1) * C + (sx - 1));
    
    vector<vector<int>> d(R, vector<int>(C, -1));
    d[sy-1][sx-1] = 0;
    
    vector<int> dy = {-1, 1, 0, 0};
    vector<int> dx = {0, 0, -1, 1};
    while (!q.empty()) {
        int yx = q.front();
        y = yx / C;
        x = yx % C;
        q.pop_front();
        for (int i = 0; i < 4; i++) {
            if (c[y + dy[i]][x + dx[i]] == '.' && d[y + dy[i]][x + dx[i]] == -1) {
                d[y + dy[i]][x + dx[i]] = d[y][x] + 1;
                q.push_back((y + dy[i]) * C + (x + dx[i]));
            }
        }
    }
    
    cout << d[gy - 1][gx - 1] << endl;
}