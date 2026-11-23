#include <bits/stdc++.h>
using namespace std;

int pow(int a, int b) {
    // 繰り返し二乗法を用いて、aのb乗を求める
    int result = 1;
    while (b) {
        if (b & 1) result *= a;
        a *= a;
        b >>= 1;
    }
    return result;
}

int main() {
    int N, K;
    cin >> N >> K;

    cout << K * pow(K-1, N-1) << endl;
}