#include <bits/stdc++.h>
using namespace std;

int main() {
    int H_1, W_1, H_2, W_2;
    cin >> H_1 >> W_1 >> H_2 >> W_2;

    cout << (H_1 == H_2 || H_1 == W_2 || W_1 == H_2 || W_1 == W_2 ? "YES" : "NO") << endl;
}