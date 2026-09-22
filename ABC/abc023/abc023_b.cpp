#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    string S;
    cin >> N >> S;

    if (N % 6 == 1) {
        for (int i = 0; i < N; i++) {
            if ((i % 3 == 0 && S[i] != 'b') || (i % 3 == 1 && S[i] != 'c') || (i % 3 == 2 && S[i] != 'a')) {
                cout << -1 << endl;
                return 0;
            }
        }
    } else if (N % 6 == 3) {
        for (int i = 0; i < N; i++) {
            if ((i % 3 == 0 && S[i] != 'a') || (i % 3 == 1 && S[i] != 'b') || (i % 3 == 2 && S[i] != 'c')) {
                cout << -1 << endl;
                return 0;
            }
        }
    } else if (N % 6 == 5) {
        for (int i = 0; i < N; i++) {
            if ((i % 3 == 0 && S[i] != 'c') || (i % 3 == 1 && S[i] != 'a') || (i % 3 == 2 && S[i] != 'b')) {
                cout << -1 << endl;
                return 0;
            }
        }
    } else {
        cout << -1 << endl;
        return 0;
    }

    // Sがアクセサリーの名前として考えられる場合はKを出力
    cout << N / 2 << endl;
}