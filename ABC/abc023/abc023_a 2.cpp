#include <bits/stdc++.h>
using namespace std;

int main() {
    int X, ans = 0;
    cin >> X;

    while (X) {
        ans += X % 10;
        X /= 10;
    }

    cout<< ans << endl;
}