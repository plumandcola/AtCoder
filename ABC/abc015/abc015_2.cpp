#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, s = 0, num = 0; // s: バグの合計数, num: バグがあるソフトウェアの個数
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (A != 0) {
            s += A;
            num++;
        }
    }

    cout << (s + num - 1) / num << endl;
}