#include <bits/stdc++.h>
using namespace std;

long double calc_c(const auto& c, int n, int r) { // 二項係数nCrを返す
    if (r < 0 || r > n) return 0;
    else return c[n][r];
}

int main() {
    // 100点解法
    int N;
    cin >> N;
    vector<int> C(N);
    for (int i = 0; i < N; i++) cin >> C[i];

    vector<vector<long double>> c(N, vector<long double>(0L)); // パスカルの三角形を用いて二項係数を求める
    for (int i = 0; i < N; i++) {
        c[i].push_back(1L);
        for (int j = 1; j <= i-1; j++) c[i].push_back((c[i-1][j-1] + c[i-1][j]));
        c[i].push_back(1L);
    }

    vector<int> count(N, 0); // count[i] := C[j](0≤j<N,j≠i)のうち、C[i]の約数の個数
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (C[i] % C[j] == 0 && i != j) count[i]++;
        }
    }

    long double ans = 0;
    for (int i = 0; i < N; i++) { // C[i]のコインが最後に表を向いている確率を調べる
        for (int m = 0; m <= count[i]; m += 2) { // C[i]のコインの左に、C[i]の約数が書かれているコインがm枚(0≤m<N,m%2==0)ある確率を調べる
            for (int j = 0; j < N; j++) { // C[i]のコインが左からj+1枚目の時を調べる
                // double型にするため、1.0をかけている
                ans += (long double)calc_c(c, j, m) / (long double)calc_c(c, N - 1, count[i]) * (long double)calc_c(c, N - j - 1, count[i] - m) / (long double)N;
            }
        }
    }

    cout << fixed << setprecision(10) << ans << endl;
}