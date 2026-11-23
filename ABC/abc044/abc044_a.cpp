#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K, X, Y;
    cin >> N >> K >> X >> Y;
    cout << X * min(K, N) + Y * max(0, N - K) << endl;
}