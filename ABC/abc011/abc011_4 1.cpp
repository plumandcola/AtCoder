#include <bits/stdc++.h>
using namespace std;

int dfs(long long i, long long x, long long X, long long y, long long Y, long long D) {
    if (i == 0) {
        if (x == X && y == Y) return 1;
        else return 0;
    }

    int ans = 0;
    ans += dfs(i-1, x+D, X, y, Y, D);
    ans += dfs(i-1, x-D, X, y, Y, D);
    ans += dfs(i-1, x, X, y+D, Y, D);
    ans += dfs(i-1, x, X, y-D, Y, D);
    return ans;
}

int main() {
    // 90点解法
    long long N, D, X, Y;
    cin >> N >> D >> X >> Y;

    int ans = dfs(N, 0, X, 0, Y, D);
    double ans_double = (double)ans;
    for (int i = 0; i < N; i++) ans_double /= 4.0;
    cout << fixed << setprecision(15) << ans_double << endl;
}