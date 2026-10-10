#include <bits/stdc++.h>
using namespace std;

int pow(int a, int b) {
    // aのb乗を求める
    int result = 1;
    for (int i = 0; i < b; i++) result *= a;

    return result;
}

int main() {
    // 100点解法
    int N;
    cin >> N;
    N++; // あえて0を個数に含める

    int ans = 0;
    for (int i = 0; i < 9; i++) {
        ans += N / pow(10, i+1) * pow(10, i);
        if (N % pow(10, i+1) > 2 * pow(10, i)) {
            ans += pow(10, i);
        } else if (N % pow(10, i+1) > pow(10, i)) {
            ans += N % pow(10, i+1) - pow(10, i);
        }
    }

    cout << ans << endl;
}