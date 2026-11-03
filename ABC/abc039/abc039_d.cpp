#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> S(H);
    for (int i = 0; i < H; i++) cin >> S[i];

    vector<string> image(H, string(W, '#'));
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (S[i][j] == '.') {
                for (int h = max(0, i-1); h < min(H, i+2); h++) {
                    for (int w = max(0, j-1); w < min(W, j+2); w++) {
                        image[h][w] = '.';
                    }
                }
            }
        }
    }

    string ans = "possible";
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (S[i][j] == '#') {
                bool possible = false;
                for (int h = max(0, i-1); h < min(H, i+2); h++) {
                    for (int w = max(0, j-1); w < min(W, j+2); w++) {
                        if (image[h][w] == '#') {
                            possible = true;
                        }
                    }
                }
                if (possible == false) {
                    ans = "impossible";
                }
            }
        }
    }

    cout << ans << endl;
    if (ans == "possible") {
        for (int i = 0; i < H; i++) {
            cout << image[i] << endl;
        }
    }
}