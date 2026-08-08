#include <bits/stdc++.h>
using namespace std;

bool is_banned(long long n) {
    while (n) {
        if (n % 10 == 4 || n % 10 == 9) return true;
        n /= 10;
    }
    return false;
}

int main() {
    // 30点解法
    long long A, B;
    cin >> A >> B;

    long long ans = 0;
    for (long long i = A; i <= B; i++) {
        ans += is_banned(i);
    }

    cout << ans << endl;
}