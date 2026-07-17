#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, x, y, ans = 0;
    cin >> N >> M;
    
    vector<vector<bool>> g(N, vector<bool>(N, false)); // g[i][j] := 議員iと議員j(i<j)が知り合いかどうか
    for (int i = 0; i < M; i++) {
        cin >> x >> y;
        g[x-1][y-1] = true;
    }
    
    for (int b = 0; b < (1 << N); b++) { // bit全探索
        bool ok = true;
        int popcount = 0;
        for (int i = 0; i < N; i++) {
            if (((b >> i) & 1) == 0) continue;
            
            popcount++;

            for (int j = i+1; j < N; j++) {
                if (((b >> j) & 1) == 0) continue;
                
                if (g[i][j] == false) ok = false; // 議員iと議員jがともに派閥に属するが、知り合いでない
            }
        }

        if (ok == true) ans = max(ans, popcount);
    }
    
    cout << ans << endl;
}