#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    else return gcd(b, a % b);
}

int main() {
    int a, b, n;
    cin >> a >> b >> n;

    int lcm = a / gcd(a, b) * b;

    cout << (n + lcm - 1) / lcm * lcm << endl;
}