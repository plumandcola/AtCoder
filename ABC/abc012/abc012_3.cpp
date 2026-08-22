#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int n = 2025 - N;

    for (int i = 1; i <= 9; i++) {
        if (n % i == 0 && n / i <= 9) cout << i << " x " << n / i << endl;
    }
}