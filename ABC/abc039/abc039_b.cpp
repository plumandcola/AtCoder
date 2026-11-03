#include <bits/stdc++.h>
using namespace std;

int main() {
    int X;
    cin >> X;

    int ans = 1;
    while (ans * ans * ans * ans != X) ans++;

    cout << ans << endl;
}