#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M = 3, count = 0; // Mは選べる数字の上限、countは処理を何回行ったか
    cin >> N;
    vector<int> NG(3);
    for (int i = 0; i < 3; i++) cin >> NG[i];

    if (find(NG.begin(), NG.end(), N) != NG.end()) { // NがNG数字の場合
        cout << "NO" << endl;
        return 0;
    }

    while (N > 0) {
        for (int i = M; i > 0; i--) {
            if (find(NG.begin(), NG.end(), max(0, N - i)) == NG.end()) {
                N = max(0, N - i);
                count++;
                break;
            }
            if (i == 1) { // 行き先が全てNG数字の場合
                cout << "NO" << endl;
                return 0;
            }
        }
    }

    if (N == 0 && count <= 100) cout << "YES" << endl;
    else cout << "NO" << endl;
}