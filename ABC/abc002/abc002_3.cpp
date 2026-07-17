#include <bits/stdc++.h>
using namespace std;

int main() {
    int x_a, y_a, x_b, y_b, x_c, y_c;
    cin >> x_a >> y_a >> x_b >> y_b >> x_c >> y_c;
    cout << fixed << abs((x_b - x_a) * (y_c - y_a) - (y_b - y_a) * (x_c - x_a)) / 2.0 << endl;
}