#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int r = a % b;
    if (r == 0) cout << 0 << endl;
    else cout << b - r << endl;
}