#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    if (n > 12) n -= 12;

    double degree = abs((30*n + m/2.0) - (6*m));

    cout << min(degree, 360 - degree) << endl;
}