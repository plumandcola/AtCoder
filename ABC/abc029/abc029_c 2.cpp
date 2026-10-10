#include <bits/stdc++.h>
using namespace std;

int pow(int a, int b) {
    // aのb乗を求める
    int result = 1;
    for (int i = 0; i < b; i++) result *= a;

    return result;
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < pow(3, N); i++) {
        for (int j = N-1; j >= 0; j--) {
            char c = 'a' + i / pow(3, j) % 3;
            cout << c;
        }
        cout << endl;
    }
}