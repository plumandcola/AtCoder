#include <bits/stdc++.h>
using namespace std;

int count(int n) {
    int result = 0;
    while (n) {
        result += (n % 10 == 1);
        n /= 10;
    }
    return result;
}

int main() {
    // 20点解法
    int N;
    cin >> N;

    int ans = 0;
    for (int i = 1; i <= N; i++) {
        ans += count(i);
    }

    cout << ans << endl;
}