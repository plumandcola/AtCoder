#include <bits/stdc++.h>
using namespace std;

int main() {
    int a, b, n;
    cin >> a >> b >> n;

    int l = lcm(a, b);

    cout << (n + l - 1) / l * l << endl;
}