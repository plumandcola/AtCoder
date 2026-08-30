#include <bits/stdc++.h>
using namespace std;

bool dfs(int n, const int& k, const vector<vector<int>>& T, const int& x) {
    // x: 今までのxorの累積
    if (n == 0) { // 全ての質問を探索した
        if (x == 0) return true; // 排他的論理和が0になる選択肢の組み合わせがあった
        else return false;
    }

    bool result = false;
    for (const int& t : T[n-1]) {
        result |= dfs(n-1, k, T, x ^ t);
        // 論理和を用いているので、排他的論理和が0になる選択肢の組み合わせが1つでもあればtrueになる
    }
    return result;
}

int main() {
    int N, K;
    cin >> N >> K;
    vector<vector<int>> T(N, vector<int>(K));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < K; j++) {
            cin >> T[i][j];
        }
    }

    cout << (dfs(N, K, T, 0) ? "Found" : "Nothing") << endl;
}