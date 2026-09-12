#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int R, C, K, ans = 0;
    cin >> R >> C >> K;

    vector<string> s(R);
    for (int i = 0; i < R; i++) cin >> s[i];

    for (int x = K-1; x <= R-K; x++) {
        for (int y = K-1; y <= C-K; y++) {
            bool flag = true;
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (abs(i-x) + abs(j-y) <= K-1 && s[i][j] == 'x') {
                        flag = false;
                    }
                }
            }

            if (flag) ans++;
        }
    }

    cout << ans << endl;
}